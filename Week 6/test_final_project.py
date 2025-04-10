# test_final_project.py

import PySimpleGUI as sg
import final_project as fp  # Import your main project code

def test_add_task():
    """
    Verify that a new task is correctly added to the layout.
    Checks the number of checkboxes before and after adding a task.
    """
    window = fp.create_main_window()
    # Count existing tasks by checking keys starting with 'checkbox_'
    initial_count = sum(1 for key in window.AllKeysDict.keys() if key.startswith("checkbox_"))
    
    # Add a new task using the current task count
    fp.add_task(window, initial_count)
    
    new_count = sum(1 for key in window.AllKeysDict.keys() if key.startswith("checkbox_"))
    assert new_count == initial_count + 1, (
        f"test_add_task failed: Expected {initial_count + 1} tasks, but got {new_count}"
    )
    window.close()
    print("test_add_task passed")

def test_reset_window():
    """
    Ensure that the window resets to the initial state.
    After adding additional tasks and calling reset, the new window should have just one task.
    """
    window = fp.create_main_window()
    # Add two new tasks
    fp.add_task(window, 1)
    fp.add_task(window, 2)
    
    # Now reset the window
    new_window = fp.reset_window(window)
    
    # After a reset, there should only be the initial task with key 'checkbox_0'.
    num_tasks = sum(1 for key in new_window.AllKeysDict.keys() if key.startswith("checkbox_"))
    assert num_tasks == 1, f"test_reset_window failed: Expected 1 task after reset, but got {num_tasks}"
    new_window.close()
    print("test_reset_window passed")

def test_task_counter():
    """
    Check that the task counter increments correctly when new tasks are added.
    Verifies that each added task gets a unique key sequentially.
    """
    window = fp.create_main_window()
    # The initial task is with key 'checkbox_0'
    task_count = 1
    
    # Add three new tasks
    for _ in range(3):
        fp.add_task(window, task_count)
        task_count += 1
        
    # Expected keys for checkboxes range from 'checkbox_0' to 'checkbox_{task_count - 1}'
    expected_keys = {f"checkbox_{i}" for i in range(task_count)}
    actual_keys = {key for key in window.AllKeysDict.keys() if key.startswith("checkbox_")}
    
    assert expected_keys == actual_keys, (
        f"test_task_counter failed: Expected keys {expected_keys}, but found {actual_keys}"
    )
    window.close()
    print("test_task_counter passed")

if __name__ == "__main__":
    test_add_task()
    test_reset_window()
    test_task_counter()
