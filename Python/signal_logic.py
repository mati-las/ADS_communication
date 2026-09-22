import time

class SignalLogic:
    def __init__(self, periodT: float = 2.0):
        self.T = periodT

        self.bOK = True
        self.signal_start = False
        
        self.start_generator = time.perf_counter()
        self.start_watcher = time.perf_counter()

        self.prev_struct = None

    def _toggle_signal(self):
        self.signal_start = not self.signal_start

    def update_time_and_signal(self):
        end = time.perf_counter()
        if end - self.start_generator >= self.T / 2:
            self.start_generator = end
            self._toggle_signal()
            
        if end - self.start_watcher >= self.T * 2:
            self.bOK = False
            
        return self.signal_start

    def update_info(self, curr_struct):
            if self.prev_struct is None or not (curr_struct == self.prev_struct):
                print(f"Data_in: {curr_struct}")
                print(f"Signal_out: {self.signal_start}")
            
            if self.prev_struct is not None:
                prev_state = self.prev_struct.bHeat1
                new_state = curr_struct.bHeat1
                            
                # rising edge
                if not prev_state and new_state:
                    self.start_watcher = time.perf_counter()
                    self.bOK = True
            self.prev_struct = curr_struct
            return self.bOK


