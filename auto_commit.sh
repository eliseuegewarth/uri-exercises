#!/bin/bash
destiny="beginner"
exercise="$(ls -d */ | grep -v "begin" | cut -f 1 -d '/')"

mv ${exercise} ${destiny}/${exercise}
git add ${destiny}/${exercise}
git commit -sm "Adicionando exercício #${exercise}"
