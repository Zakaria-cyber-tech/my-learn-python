import streamlit as st

st.title("💬 Chat Demo")

# 1️⃣ Session state لتخزين الرسائل
if "messages" not in st.session_state:
    st.session_state.messages = []

# 2️⃣ دالة لتوليد رد البوت (ممكن تبدلها API)
def get_bot_reply(user_message):
    return f"رد افتراضي على: {user_message}"

# 3️⃣ Input
user_input = st.text_input("اكتب رسالتك هنا...")

# 4️⃣ زر إرسال
if st.button("إرسال") and user_input:
    # خزّن الرسائل
    st.session_state.messages.append({"user": user_input, "bot": get_bot_reply(user_input)})
    # مسح خانة الكتابة بعد الإرسال
    st.experimental_rerun()  # هادي باش textbox يرجع فارغ بعد الإرسال

# 5️⃣ عرض الرسائل
st.subheader("المحادثة:")
chat_box = st.container()  # container لعرض كل الرسائل
with chat_box:
    for msg in st.session_state.messages:
        st.markdown(f"**You:** {msg['user']}")
        st.markdown(f"**Bot:** {msg['bot']}")
        st.markdown("---")
