class BowlingGame:
    def __init__(self):
        self.frame_size = 10
        self.game_track = []
        self.final_score_sheet = []
        self.i = -1
        self.total = 0
        self.final_frame_counter = 0

    def roll(self, pins):
        self.game_track.append(pins)
        self.i += 1
        if self.game_track is not None:
            if len(self.final_score_sheet) < 10:
                if pins < self.frame_size:
                    if len(self.game_track) == 1:
                        return None
                    if self.game_track[self.i-1] != 10 and (self.game_track[self.i-1]+pins) <= 10:
                        self.final_score_sheet.append(pins+self.game_track[self.i-1])
                    elif (self.game_track[self.i-1]+pins) > 10:
                        raise ValueError("invalid fill balls")
                else:
                    self.final_score_sheet.append(10)
            else:
                # Deal with special 10th case
                temp = 0
                if self.final_frame_counter > 4:
                    raise IndexError("cannot throw bonus with an open tenth frame")

                if pins < 10:
                    temp += pins
                    if temp > 10:
                        raise ValueError("invalid fill balls")
                    else:
                        self.total += temp
                        self.final_frame_counter += 1
                else:
                    self.total += 10
                    self.final_frame_counter += 1

                if self.final_frame_counter == 3:
                    self.final_score_sheet.append(self.total)


    def score(self):
        if self.final_score_sheet is not None:
            final = 0
            for each_item in self.final_score_sheet:
                final += each_item
            if final > 0:
                return final
            else:
                raise ValueError("invalid fill balls")
        else:
            raise ValueError("invalid fill balls")
