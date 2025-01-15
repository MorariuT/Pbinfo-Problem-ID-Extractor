# Pbinfo-Problem-ID-Extractor
A tool writen in python that takes all problems from pbinfo.ro and transforms them into $2$ maps: `title_to_id` and `id_to_title`

The tool makes some simple steps:
  * Iterate an $i$ from $1$ to $4000$
  * `GET` the `URL` specific to the problem with this `ID`
  * Check if the `ID` is avalible
  * If yes put it in the map
  * Write the maps to two files
