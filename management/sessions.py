

def encode(self, session_dict):
    "Returns the given session dictionary pickled and encoded as a string."
    pickled = pickle.dumps(session_dict, pickle.HIGHEST_PROTOCOL)
    hash = self._hash(pickled)
    h = hash()
    return base64.encodestring(hash + ":" + pickled)