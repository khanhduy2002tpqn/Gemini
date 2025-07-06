import streamlit as st
import google.generativeai as genai

# --- Cấu hình API Key ---
st.set_page_config(page_title="IELTS Writing Evaluator", layout="centered")

st.title("📝 IELTS Writing Evaluator with Gemini")
api_key = "Nhập api key tại dây"

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash-002",generation_config=generation_config)

        prompt_prefix = """
Bạn là một giám khảo IELTS Writing. Nhiệm vụ của bạn là:

1. Đọc bài viết.
2. Chấm điểm theo từng tiêu chí của IELTS Writing Task 2:
   - Task Response
   - Coherence and Cohesion
   - Lexical Resource
   - Grammatical Range and Accuracy
3. Đưa ra điểm số từng phần (0.0–9.0) và tổng điểm trung bình.
4. Góp ý để cải thiện bài viết.

Dưới đây là bài viết:
        """

        user_essay = st.text_area("✍️ Nhập bài viết IELTS Writing Task 2 của bạn tại đây:")

        if st.button("📊 Đánh giá bài viết"):
            with st.spinner("Đang chấm điểm..."):
                response = model.generate_content(prompt_prefix + user_essay)
                st.subheader("📋 Kết quả đánh giá")
                st.markdown(response.text)

    except Exception as e:
        st.error(f"Lỗi khi kết nối API: {e}")
else:
    st.info("Hãy nhập API Key để bắt đầu.")
