from .base import ArgType, BaseOpcode, OpcodeArg


class MusicControlOpcode(BaseOpcode):

    opcode = 0x5C
    name = "MUSIC_CONTROL"

    def get_args(self):
        return [
            OpcodeArg("control_type", ArgType.BYTE, 1, "Music control mode"),
            OpcodeArg("song_id", ArgType.WORD, 2, "Song/track ID"),
        ]

    def calculate_length(self, data: bytes, offset: int) -> int:
        if offset + 2 > len(data):
            return 1

        control_type = data[offset + 1]
        if control_type & 0x80:
            return 6
        elif control_type >= 0xA0:
            return 6
        else:
            return 4

    def get_legible_representation(self, raw_bytes: bytes, args=None, context=None):

        control_type = args["control_type"]
        song_id = args["song_id"]

        song_work_area = self.format_work_area_value(song_id, context=context)
        song_id_str = f"song {song_work_area}"

        music_slots = {
            0x00: "Idle (Day)",
            0x01: "Idle (Night)",
            0x02: "Combat (Solo)",
            0x03: "Combat (Party)",
            0x04: "Chocobo/Mount",
            0x05: "Death",
            0x06: "Music Slot 6",
            0x07: "Music Slot 7",
        }

        if control_type in music_slots:
            slot_name = music_slots[control_type]
            return f"MUSIC_CONTROL: Set {slot_name} music to {song_id_str}"
        elif control_type >= 0x80 and control_type <= 0x87:
            slot_index = control_type - 0x80
            slot_name = music_slots.get(slot_index, f"Music Slot {slot_index}")
            if len(raw_bytes) >= 6:
                import struct

                volume = struct.unpack_from("<H", raw_bytes, 4)[0]
                volume_str = self.format_work_area_value(volume, context=context)
                return f"MUSIC_CONTROL: Set {slot_name} music to {song_id_str}, volume={volume_str}"
            else:
                return f"MUSIC_CONTROL: Set {slot_name} music to {song_id_str} with volume"
        elif control_type == 0xA0 or control_type == 0xA1:
            if len(raw_bytes) >= 6:
                import struct

                fade_time = struct.unpack_from("<H", raw_bytes, 4)[0]
                fade_str = self.format_work_area_value(fade_time, context=context)
                if control_type == 0xA0:
                    return f"MUSIC_CONTROL: Set music volume to {song_id_str}, fade_time={fade_str}"
                else:
                    return f"MUSIC_CONTROL: Adjust music volume to {song_id_str}, fade_time={fade_str}"
            else:
                return f"MUSIC_CONTROL: Volume control {control_type:02X}"
        else:
            return f"MUSIC_CONTROL: Unknown control type 0x{control_type:02X}, song_id={song_id_str}"
