import os
from PIL import Image
import streamlit as st 


import detection
import constants


def main():
	"""Face Detection App"""

	st.title("Face Detection App")
	st.text("By :- Aabid Umer")

	activities = ["Detection"]
	choice = st.sidebar.selectbox("Select Activty",activities)

	if choice == 'Detection':
		st.subheader("Face Detection")

		image_file = st.file_uploader("Upload Image",type=['jpg','png','jpeg'])

		if image_file is not None:
			our_image = Image.open(image_file)
			st.text("Original Image")
			st.write(type(our_image))
			st.image(our_image)
        

		# Face Detection
		task = ["Faces"]
		feature_choice = st.sidebar.selectbox("Find Features",task)
		if st.button("Process"):
			if feature_choice == 'Faces':
				result_img,result_faces = detection.detect_faces(our_image)
				st.image(result_img)

				st.success("Found {} faces".format(len(result_faces)))


if __name__ == '__main__':
		main()	