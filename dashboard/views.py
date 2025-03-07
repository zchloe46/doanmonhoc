# -*- coding: utf-8 -*-
from django.shortcuts import render
from underthesea import word_tokenize, pos_tag, classify

def dashboard_view(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        tokens = word_tokenize(text)
        tagged = pos_tag(text)
        sentiment = classify(text)[0]  # Lấy giá trị đầu tiên trong danh sách
        #
        # Loại bỏ dấu gạch dưới và viết hoa chữ cái đầu tiên
        sentiment_formatted = sentiment.replace('_', ' ').capitalize()

        context = {
            'text': text,
            'tokens': tokens,
            'tagged': tagged,
            'sentiment': sentiment_formatted,  # Truyền sentiment đã được định dạng
        }
        return render(request, 'dashboard.html', context)
    return render(request, 'dashboard.html')