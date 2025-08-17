# 17772586 - Perisa-Neburusa

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 144 bytes                 |
| Total Events     | 2                         |
| References Count | 9                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [76](#event-76)       | 0x0001       |     82 |             25 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0003      |           3 |
|       1 | 0x2704      |        9988 |
|       2 | 0x2705      |        9989 |
|       3 | 0x2706      |        9990 |
|       4 | 0x0000      |           0 |
|       5 | 0x2707      |        9991 |
|       6 | 0x0001      |           1 |
|       7 | 0x2708      |        9992 |
|       8 | 0x40000000  |  1073741824 |

## String References

- **9988**: This is the entrance to Jeuno's Rent-a-Rooms. Press the button near the central pillar to go inside.
- **9989**: This is the entrance to Jeuno's residential area. Do you want to move your belongings to a Rent-a-Room here?
- **9990**: Do you want to move to Jeuno? [Yes./No.]
- **9991**: Very well. I've completed the necessary procedures. You'll find a button near the central pillar. Press it to enter.
- **9992**: If you ever feel like moving, just ask me.

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 76

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 82 bytes |
| Instructions | 25       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  03 00 00 02 10 02 00 00   .....op........
0010: 00 80 00 1C 00 1D 01 80  23 01 51 00 1D 02 80 23  ........#.Q....#
0020: 24 03 80 04 80 04 80 25  02 00 10 04 80 00 3D 00  $......%......=.
0030: 42 1D 05 80 23 03 01 10  04 80 01 51 00 02 00 10  B...#......Q....
0040: 06 80 00 51 00 1D 07 80  23 03 01 10 08 80 01 51  ...Q....#......Q
0050: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  4: 0x000D [0x02] IF !(ExtData[1]->WorkLocal[0] == 3*) GOTO 0x001C
  5: 0x0015 [0x1D] PRINT_EVENT_MESSAGE(message_id=9988*)
    → "This is the entrance to Jeuno's Rent-a-Rooms. Press the button near the central pillar to go inside."
  6: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0019 [0x01] GOTO 0x0051
  8: 0x001C [0x1D] PRINT_EVENT_MESSAGE(message_id=9989*)
    → "This is the entrance to Jeuno's residential area. Do you want to move your belongings to a Rent-a-Room here?"
  9: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0020 [0x24] CREATE_DIALOG(message_id=9990*, default_option=0*, option_flags=0*)
    → "Do you want to move to Jeuno? [Yes./No.]"
 11: 0x0027 [0x25] WAIT_DIALOG_SELECT()
 12: 0x0028 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x003D
 13: 0x0030 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 14: 0x0031 [0x1D] PRINT_EVENT_MESSAGE(message_id=9991*)
    → "Very well. I've completed the necessary procedures. You'll find a button near the central pillar. Press it to enter."
 15: 0x0034 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0035 [0x03] Work_Zone[1] = 0*
 17: 0x003A [0x01] GOTO 0x0051
 18: 0x003D [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0051
 19: 0x0045 [0x1D] PRINT_EVENT_MESSAGE(message_id=9992*)
    → "If you ever feel like moving, just ask me."
 20: 0x0048 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x0049 [0x03] Work_Zone[1] = 1073741824*
 22: 0x004E [0x01] GOTO 0x0051

SUBROUTINE_0051:
 23: 0x0051 [0x21] END_EVENT
 24: 0x0052 [0x00] END_REQSTACK()
```
