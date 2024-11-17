"""Functions to help Azara and Rui locate pirate treasure."""
def get_coordinate(record):
    return record[-1]
    
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.
 
    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    pass
def convert_coordinate(coordinate):
    return tuple(coordinate)
    """Split the given coordinate into tuple containing its individual components.
 
    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    pass
def compare_records(azara_record, rui_record):
    azara_coordinate = tuple(azara_record[1])
    return azara_coordinate == rui_record[1]
    
    #return tuple(azara_record[1]) == rui_record[1]
   
        
    """Compare two record types and determine if their coordinates match.
 
    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    pass
def create_record(azara_record, rui_record):
    
    azara_coordinate = tuple(azara_record[1])
    if azara_coordinate == rui_record[1]:
        return azara_record + rui_record
    else:
        return "not a match" 
   
    """Combine the two record types (if possible) and create a combined record group.
 
    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    pass
def clean_up(combined_record_group):
    result = ""
    for record in combined_record_group: 
         result += str(record[:1] + record[2:]) + "\n"
    return result
    """Clean up a combined record group into a multi-line string of single records.
 
    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.
 
    The return statement should be a multi-lined string with items separated by newlines.
 
    (see HINTS.md for an example).
    """
    pass
