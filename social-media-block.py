import pyuac
import sys # This module needs for admin code


class AdminTaskRunner:
    """
    #using pyuac admin role 
    """

    def __init__(self):
        """Automatically checkj for admin"""
        print("AdminTaskRunner starting...")
        #We check user is admin or not
        if not pyuac.isUserAdmin():
            print("User is not admin! Restarting with admin rights!")
            # runAsAdmin stops for admin rights and then restarts
            # python sessien end
            pyuac.runAsAdmin()
            # if reboot okay it will not come here
            sys.exit(0) 
        else:        
            print("This program running admin")
            input("running as admin press enter to continue!")

    def run_admin_operations(self):
        
        return


# --- Basic usage ---
if __name__ == "__main__":
    
    # 1. class.
    # __init__ metod starts admin
    # 
    runner = AdminTaskRunner()
    
    # 2. Method for admin rights
    # Only you can access admin rights
    runner.run_admin_operations()