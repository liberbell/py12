import face_recognition

# Load the known images
image_of_person_1 = face_recognition.load_image_file("person_1.jpg")
image_of_person_2 = face_recognition.load_image_file("person_2.jpg")
image_of_person_3 = face_recognition.load_image_file("person_3.jpg")

# Get the face encoding of each person. This can fail if no one is found in the photo.




# Create a list of all known face encodings
known_face_encodings = [



]

# Load the image we want to check


# Get face encodings for any people in the picture


# There might be more than one person in the photo, so we need to loop over each face we found
for unknown_face_encoding in unknown_face_encodings:

    # Test if this unknown face encoding matches any of the three people we know


    name = "Unknown"

    if results[0]:
        name = "Person 1"
    elif results[1]:
        name = "Person 2"
    elif results[2]:
        name = "Person 3"

    print(f"Found {name} in the photo!")
