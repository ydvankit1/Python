def serveFood(item):
    try:
        print(f"preparing {item}....")
        if(item=="unknown"):
            raise ValueError("we dont have this food item")
    except ValueError as e:
        print("Error: ", e)
    else:
        print(f"{item} is served")
    finally:
        print("next order please....")


serveFood("Paneer")
serveFood("unknown")
