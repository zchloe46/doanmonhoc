from django.shortcuts import render
from underthesea import word_tokenize, pos_tag, classify


def dashboard_view(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        # Tách từ
        tokens = word_tokenize(text)
        # Gán nhãn từ loại
        tagged = pos_tag(text)
        # Phân loại văn bản (tích cực/tiêu cực)
        sentiment = classify(text)  # Trả về list, ví dụ: ['positive'] hoặc ['negative']

        context = {
            'text': text,
            'tokens': tokens,
            'tagged': tagged,
            'sentiment': sentiment[0],  # Lấy giá trị đầu tiên trong danh sách
        }
        return render(request, 'dashboard.html', context)
    return render(request, 'dashboard.html')