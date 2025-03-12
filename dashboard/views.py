from django.shortcuts import render
from underthesea import classify, word_tokenize, pos_tag

# Định nghĩa ánh xạ cho các giá trị sentiment
sentiment_mapping = {
    'the_thao': 'Thể thao',
    'phap_luat': 'Pháp luật',
    'the_gioi': 'Thế giới',
    'doi_song': 'Đời sống',
    'chinh_tri_xa_hoi': 'Chính trị Xã hội',
    'vi_tinh': 'Vi tính',
    'khoa_hoc': 'Khoa học',
    'van_hoa': 'Văn hoá',
    'kinh_doanh': 'Kinh doanh',
    'suc_khoe': 'Sức khỏe',
    'khac': 'Khác',
    'tich_cuc': 'Tích cực',
    'tieu_cuc': 'Tiêu cực',
    'trung_lap': 'Trùng lặp',
    'khong_y_kien': 'Không ý kiến',
    'pho_bien': 'Phổ biến',
    'sai': 'Sai',

}


def dashboard_view(request):
    return render(request, 'dashboard.html')


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
            sentiment = classify(text)[0].replace('_', ' ').capitalize()
            sentiment_display = sentiment_mapping.get(sentiment, sentiment)
            sentiment_formatted = sentiment_display.replace('_', ' ').capitalize()
            context['sentiment'] = sentiment_formatted
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
            tokens = word_tokenize(text)
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
            tagged = pos_tag(text)
            context['tagged'] = tagged
            context['text'] = text
    return render(request, 'pos_tag.html', context)

# def dashboard_view(request):
#     if request.method == 'POST':
#         text = request.POST.get('text', '')
#         tokens = word_tokenize(text)
#         tagged = pos_tag(text)
#         sentiment = classify(text)[0]  # Lấy kết quả phân loại
#
#         # Ánh xạ sang giá trị có dấu và định dạng
#         sentiment_display = sentiment_mapping.get(sentiment, sentiment)
#         sentiment_formatted = sentiment_display.replace('_', ' ').capitalize()
#
#         context = {
#             'text': text,
#             'tokens': tokens,
#             'tagged': tagged,
#             'sentiment': sentiment_formatted,  # Truyền giá trị đã định dạng
#         }
#         return render(request, 'dashboard.html', context)
#     return render(request, 'dashboard.html')