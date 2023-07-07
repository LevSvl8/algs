

states_needed = set(['az','ca','or','nv','ut','id','wa','mt'])

stations = {}
stations['kone'] = set(['id','nv','ut'])
stations['kwo'] = set(['wa','mt','id'])
stations['kthree'] = set(['or','nv','ka'])
stations['kfour'] = set(['nv','ut'])
stations['kfive'] = set(['ca','az'])

final_stations = set()

while states_needed.__len__():
    states_covered = set()
    best_station = None
    for station,states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = states_for_station
            final_stations.add(station)
            states_needed = states_needed - states_for_station
print final_stations