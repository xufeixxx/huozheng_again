from overall.list import userPoint_list
from overall.settings import Settings

setts = Settings()


# self.map_width = [-166.524881, 145.003318]  # 经度
# self.map_length = [30.000060, 59.999807]  # 纬度


def space_range_size(size):
    try:
        new_width_end = setts.map_width[0] + size * (setts.map_width[1] - setts.map_width[0])
        original_result = 0
        disturb_result = 0
        mw0 = setts.map_width[0]
        ml0 = setts.map_length[0]
        ml1 = setts.map_length[1]
        for user in userPoint_list:
            if user.in_voronoiCell:
                if mw0 <= user.u_longitude <= new_width_end and ml0 <= user.u_latitude <= \
                        ml1:
                    original_result += 1
                if mw0 <= user.send_longitude <= new_width_end and ml0 \
                        <= user.send_latitude <= ml1:
                    disturb_result += 1

        return (abs(original_result - disturb_result)) / original_result
    except ZeroDivisionError:
        print("You can't divide by zero!")