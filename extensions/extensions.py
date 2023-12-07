file_name = input("Enter file name: ").lower().strip()
extension = file_name.split(".")[-1]

match extension:
    case "jpeg" | "gif" | "png":
        print(f"image/{extension}")
    case "jpg":
        print("image/jpeg")
    case "pdf" | "zip":
        print(f"application/{extension}")
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")