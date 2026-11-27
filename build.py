import os
# i parameterise this one
message = os.getenv("BUILD_MESSAGE", "Hi Nanba")
print("Jnekins build")
print(f"Build Message: {message}")
print("Build done success")