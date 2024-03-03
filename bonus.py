from abc import ABC, abstractmethod
#(SRP) There are seperate classes for User, representing the user, Activity, representing an activity, ActivityMoniter, monitoring activities, DataStorage, storing data, and Display for displaying data 
#seperate interfaces for data storage and display because they configure different tasks or concerns. Data Storage can only be used to save data and Display can only be used to display data(ISP)
#(OCP and LSP) Any new activity type can easily by adding by creating a subclass of activity without having to change any of the other classes because the activity would just require the method collecting data which is the abstract method in Activity
#(LSP) Allowing for a loosely coupled system the activity class and subclasses can act independently without having the activity monitor being active, and the other way around
class DataStorage(ABC):
    @abstractmethod
    def save_data(self, user_id, activity_type, data):
        pass

class Display(ABC):
    @abstractmethod
    def display_data(self, user_id, activity_type, data):
        pass
#initialized user object with their id
class User:
    def __init__(self, user_id):
        self.user_id = user_id
#parent class to all new activity subclasses with the concrete collect_data method, used in all subclasses
class Activity(ABC):
    def __init__(self, user_id):
        self.user_id = user_id
    
    @abstractmethod
    def collect_data(self):
        pass
# can update step activity in main
class StepsActivity(Activity):
    def __init__(self, user_id, initial_steps = 0):
        super().__init__(user_id)
        self.steps_data = {"steps": initial_steps}
    def collect_data(self):
        return self.steps_data
    def update_steps(self, new_steps):
        self.steps_data["steps"] = new_steps\
#can update distance activity in main
class DistanceActivity(Activity):
    def __init__(self, user_id, initial_distance = 0):
        super().__init__(user_id)
        self.distance_data = {"distance": initial_distance}
    def collect_data(self):
        return self.distance_data
    def update_distance(self, new_distance):
        self.distance_data["distance"] = new_distance
# can update calories burned in main
class CaloriesBurnedActivity(Activity):
    def __init__(self, user_id, initial_calories = 10):
        super().__init__(user_id)
        self.calories_data = {"calories": initial_calories}

    def collect_data(self):
        return self.calories_data
    
    def update_calories(self, new_calories):
        self.calories_data["calories"] = new_calories

    
#(DIP) To create an activity monitor object,in the constructor, there are dependencies for a data storage and display object, then the attributes are set to equal the objects 
class ActivityMonitor:
    def __init__(self, user, data_storage: DataStorage, display: Display):
        self.user = user
        self.data_storage = data_storage #initializes with data_storage object
        self.display = display #initializes with display object
#(OCP) Observer pattern is used because the activity monitor observes activity and updates display when new data is collected, by making the activity object a dependency when calling the monitor activity module and using the method display_data in the activity monitor module with the objects attributes
    def monitor_activity(self, activity: Activity):
        data = activity.collect_data()
        activity_type = activity.__class__.__name__
        self.data_storage.save_data(self.user.user_id, activity_type, data) #updating the data storage when data collected
        self.display.display_data(self.user.user_id, activity_type, data)  #updating the display when data collected

#writes new data to a file with data storage interface
class Data(DataStorage):
    def save_data(self, user_id, activity_type, data):
        with open(f"{user_id}_{activity_type}_data.txt", "a") as file:
            file.write(str(data)+ "\n")

#writes activity data from monitor to screen with display interface
class Screen(Display):
    def display_data(self, user_id, activity_type, data):
        print(f"User {user_id}: {activity_type} - {data}")

def main():
    user = User(user_id = 234)
    data_storage = Data()
    display = Screen()

    activity_monitor = ActivityMonitor(user, data_storage, display)

    steps_activity = StepsActivity(user.user_id)
    activity_monitor.monitor_activity(steps_activity)

    distance_activity = DistanceActivity(user.user_id)
    activity_monitor.monitor_activity(distance_activity)

    calories_activity = CaloriesBurnedActivity(user.user_id)
    activity_monitor.monitor_activity(calories_activity)

    new_calories = 150
    calories_activity.update_calories(new_calories)
    activity_monitor.monitor_activity(calories_activity)

    new_steps = 500
    steps_activity.update_steps(new_steps)
    activity_monitor.monitor_activity(steps_activity)

    new_distance = 1.5
    distance_activity.update_distance(new_distance)
    activity_monitor.monitor_activity(distance_activity)
if __name__ == "__main__":
    main()