seconds = int(input("Enter the duration in seconds:\n"))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60
print(
    f"The duration is: {hours} hours, {minutes}, minutes, and {remaining_seconds} seconds."
)
