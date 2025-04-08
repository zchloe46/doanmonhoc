from django.shortcuts import render
from underthesea import word_tokenize, pos_tag, classify

from .models import Contact, Test, VanBan, PhanLoai, TachTu, GanNhan


sentiment_mapping = {
                'Pháp luật': 'phapluat',
                'Kinh tế': 'kinhte',
                'Giáo dục': 'giaoduc',
                'Thể thao': 'thethao',
                'Thế giới': 'thegioi',
                'Sức khỏe': 'suckhoe',
                'Văn hóa': 'vanhoa',
                'Xã hội': 'xahoi',
                'Công nghệ': 'congnghe',
                'Du lịch': 'dulich',
                'Thời trang': 'thoitrang',
                'Giải trí': 'giaitri',
                'Tâm sự': 'tamsu',
                'Ẩm thực': 'amthuc',
                'Xe': 'xe',
                'Bất động sản': 'batdongsan',
                'Nông nghiệp': 'nongnghiep',
                'Môi trường': 'moitruong',
                'Tài chính': 'taichinh',
                'Khởi nghiệp': 'khoinghiep',
                'Bảo hiểm': 'baohiem',
                'Thương mại điện tử': 'thuongmaidientu',
                'Truyền thông': 'truyenthong',
                'Khoa học': 'khoahoc',
                'Giải trí': 'giaitri',
            }

def dashboard_view(request):
    return render(request, 'dashboard.html')

def about_view(request):
    return render(request, 'about.html')
def learn_view(request):
    return render(request, 'learn.html')

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
            sentiment = classify(text)[0].replace('_', ' ').capitalize()
            # ánh xạ kết quả phân loại như: Pháp luật (hiển thị) -> phapluat (trong DB)
            

            # Lưu vào bảng vanban trong DB
            test_entry = Test.objects.create(
                content=text,
                resultTachTu=tokens,
                resultGanNhan=tagged,
                resultPhanLoai=sentiment
            )

            # Truyền kết quả vào context để hiển thị trên giao diện
            context['text'] = text
            context['tokens'] = result_tach_tu
            context['tagged'] = tagged
            context['sentiment'] = sentiment
            context['success'] = True

    return render(request, 'test.html', context)
    
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
            # Lưu văn bản vào bảng van_ban
            van_ban = VanBan.objects.create(content=text)
            # Thực hiện phân loại
            sentiment = classify(text)[0].replace('_', ' ').capitalize()
            # Lưu kết quả vào bảng phan_loai
            # PhanLoai.objects.create(idVB=van_ban, resultPhanloai=sentiment)
            context['sentiment'] = sentiment
            context['text'] = text
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
            # Lưu văn bản vào bảng van_ban
            van_ban = VanBan.objects.create(content=text)
            # Thực hiện tách từ
            tokens = word_tokenize(text)
            # Lưu kết quả vào bảng tach_tu
            # TachTu.objects.create(idVB=van_ban, resultTachtu=str(tokens))
            context['tokens'] = tokens
            context['text'] = text
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
            # Lưu văn bản vào bảng van_ban
            van_ban = VanBan.objects.create(content=text)
            # Thực hiện gán nhãn
            tagged = pos_tag(text)
            # Lưu kết quả vào bảng gan_nhan
            # GanNhan.objects.create(idVB=van_ban, resultGannhan=str(tagged))
            context['tagged'] = tagged
            context['text'] = text
    return render(request, 'pos_tag.html', context)

