from sys import argv

class NotSymmetricError(Exception):
    pass

def main():
    try:
        queue = []
        brackets = {"{": "}", "(": ")", "[": "]"}
        d = "".join(argv[1]).lower().strip()
        print(d)

        def remove_from_queue(item):
            if len(queue) > 0:
                queue_item = queue.pop()
                print(f"Removing matching opening {item} from queue")
                if item != brackets[queue_item]:
                    raise NotSymmetricError
            else:
                raise NotSymmetricError


        for i in range(len(d)):
            print(f"queue: {queue}")
            if d[i] in brackets.keys():
                print(f"Adding {d[i]} to queue")
                queue.append(d[i])
            elif d[i] in brackets.values():
                remove_from_queue(d[i])

        if len(queue) == 0:
            print("The string is symmetric.")
        else:
            raise NotSymmetricError
    except IndexError:
        print("Please provide a string as a 2nd command-line argument in quotes")
    except NotSymmetricError:
        print("The string is not symmetric.")


if __name__ == '__main__':
    main()