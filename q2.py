from flask import Flask, request, make_response #flask 2.0.3
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

@app.route('/image', methods=['GET'])

def generate_image():
    # 取得寬度和高度參數
    width = int(request.args.get('width'))
    height = int(request.args.get('height'))
    # 產生隨機顏色的 numpy 陣列
    img_array = np.random.rand(height, width, 3) * 255
    # 將 numpy 陣列轉換成 PIL 的 Image 物件
    img = Image.fromarray(np.uint8(img_array))
    # 將 PIL 的 Image 物件轉換成 BytesIO 物件
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    # 將 BytesIO 物件轉換成二進制字串
    img_binary = img_bytes.getvalue()
    # 回傳圖片
    response = make_response(img_binary)
    response.headers.set('Content-Type', 'image/png')
    return response

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)
