from django.shortcuts import render
from underthesea import word_tokenize, pos_tag, classify

from .models import Contact, Test


sentiment_mapping = {
                'the_thao': 'Thể thao',
                'phap_luat': 'Pháp luật',
                'the_gioi': 'Thế giới',
                'doi_song': 'Đời sống',
                'chinh_tri_xa_hoi': 'Chính trị xã hội',
                'vi_tinh': 'Vi tính',
                'khoa_hoc': 'Khoa học',
                'van_hoa': 'Văn hóa',
                'kinh_doanh': 'Kinh doanh',
                'suc_khoe': 'Sức khỏe'
}

def dashboard_view(request):
    return render(request, 'dashboard.html')

def about_view(request):
    return render(request, 'about.html')


def test_view(request):
    context = {}
    if request.method == 'POST':
        # Lấy văn bản từ form
        if 'text' in request.POST:
            text = request.POST.get('text', '')
        elif 'file' in request.FILES:
            file = request.FILES['file']
            text = file.read().decode('utf-8')
        else:
            text = ''

        if text:
            # Thực hiện tách từ
            tokens = word_tokenize(text)    
            result_tach_tu = ' | '.join(tokens)

            # Thực hiện gán nhãn
            tagged = pos_tag(text)
            result_gan_nhan = ', '.join([f"{word}/{tag}" for word, tag in tagged])

            # Thực hiện phân loại
            sentiment = classify(text)[0]
            result_phan_loai = sentiment_mapping.get(sentiment, sentiment.capitalize())  # Chuyển đổi nhãn phân loại thành tên dễ đọc

            # Lưu vào bảng vanban trong DB
            db = Test.objects.create(
                content=text,
                resultTachTu=tokens,
                resultGanNhan=tagged,
                resultPhanLoai=result_phan_loai
            )

            # Truyền kết quả vào context để hiển thị trên giao diện
            context['text'] = text
            context['tokens'] = result_tach_tu
            context['tagged'] = tagged
            context['sentiment'] = result_phan_loai
            context['success'] = True

    return render(request, 'test.html', context)  # trả về template test.html
    
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        Contact.objects.create(name=name, email=email, phone= phone, message=message)
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')

def classify_view(request):
    context = {}
    if request.method == 'POST':
        if 'text' in request.POST:
            text = request.POST.get('text', '')
        elif 'file' in request.FILES:
            file = request.FILES['file']
            text = file.read().decode('utf-8')
        else:
            text = ''
        
        if text:
            # Thực hiện phân loại
            sentiment = classify(text)[0]
            result_phan_loai = sentiment_mapping.get(sentiment, sentiment)
            context['sentiment'] = result_phan_loai
            context['text'] = text
            context['success'] = True
    return render(request, 'classify.html', context)

def tokenize_view(request):
    context = {}
    if request.method == 'POST':
        if 'text' in request.POST:
            text = request.POST.get('text', '')
        elif 'file' in request.FILES:
            file = request.FILES['file']
            text = file.read().decode('utf-8')
        else:
            text = ''
        
        if text:    
            # Thực hiện tách từ
            tokens = word_tokenize(text)
            context['tokens'] = tokens
            context['text'] = text
            context['success'] = True
    return render(request, 'tokenize.html', context)

def pos_tag_view(request):
    context = {}
    if request.method == 'POST':
        if 'text' in request.POST:
            text = request.POST.get('text', '')
        elif 'file' in request.FILES:
            file = request.FILES['file']
            text = file.read().decode('utf-8')
        else:
            text = ''
        
        if text:
            # Thực hiện gán nhãn
            tagged = pos_tag(text)
            context['tagged'] = tagged
            context['text'] = text
            context['success'] = True
    return render(request, 'pos_tag.html', context)

