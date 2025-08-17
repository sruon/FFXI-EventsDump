# 17797124 - Mauh Halaapah

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Mhaura (ID: 249) |
| Block Size       | 476 bytes        |
| Total Events     | 3                |
| References Count | 15               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [41](#event-41)       | 0x0001       |     28 |              8 |
| [40](#event-40)       | 0x001D       |    358 |             48 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0032      |          50 |
|       1 | 0x1BC8      |        7112 |
|       2 | 0x1AC5      |        6853 |
|       3 | 0x1AC0      |        6848 |
|       4 | 0x0000      |           0 |
|       5 | 0x1AC6      |        6854 |
|       6 | 0x00C8      |         200 |
|       7 | 0x0095      |         149 |
|       8 | 0x079C      |        1948 |
|       9 | 0x0034      |          52 |
|      10 | 0x1AC7      |        6855 |
|      11 | 0x0002      |           2 |
|      12 | 0x0001      |           1 |
|      13 | 0x1AC8      |        6856 |
|      14 | 0x1AC9      |        6857 |

## String References

- **6848**: Are you new to Mhaura? [Yes, it's my first time here./No, I've come here plenty of times.]
- **6853**: Hello, therrre. I don't believe I've seen you before. You must be new in town.
- **6854**: I thought so. Welcome to Mhaura! Visitors like you should go to the governor's house to get an orientation.
- **6855**: Go up the stairs at the western end of this square, then up again the stairrrs on your left. Good luck!
- **6856**: Rrreally? I'm sorry. I'm usually good with names...
- **6857**: You should visit the governor's house if you haven't already. They will answer any questions you have about Mhaura.
- **7112**: This is a small town, but we get a lot of traffic because of the port. We have to stay alert and try to stop trrrouble before it starts.

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

### Event 41

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 21 00           ...tlk0...#!.   
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=7112*)
    → "This is a small town, but we get a lot of traffic because of the port. We have to stay alert and try to stop trrrouble before it starts."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x21] END_EVENT
  7: 0x001C [0x00] END_REQSTACK()
```

### Event 40

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x001D    |
| Data Size    | 358 bytes |
| Instructions | 48        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         1E F0 FF               ...
0020: FF 7F 6F 70 66 00 80 F8  FF FF 7F F8 FF FF 7F 74  ..opf..........t
0030: 6C 6B 30 1D 02 80 23 5E  69 64 6C 30 24 03 80 04  lk0...#^idl0$...
0040: 80 04 80 25 02 00 10 04  80 00 5A 01 42 66 00 80  ...%......Z.Bf..
0050: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 1D 05 80 23  ........tlk0...#
0060: 53 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 45 06 80  S........tlk0E..
0070: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 04 80 55 06  ........fdo1..U.
0080: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 46 01 45  .........fdo1F.E
0090: 07 80 F0 FF FF 7F F0 FF  FF 7F 73 65 30 37 04 80  ..........se07..
00A0: 45 06 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 31 04  E..........fdi1.
00B0: 80 55 06 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 31  .U..........fdi1
00C0: 39 08 80 6F 70 66 09 80  F8 FF FF 7F F8 FF FF 7F  9..opf..........
00D0: 70 6F 69 31 1D 0A 80 23  55 07 80 F0 FF FF 7F F0  poi1...#U.......
00E0: FF FF 7F 73 65 30 37 53  F8 FF FF 7F F8 FF FF 7F  ...se07S........
00F0: 70 6F 69 31 45 06 80 F0  FF FF 7F F0 FF FF 7F 66  poi1E..........f
0100: 64 6F 31 04 80 55 06 80  F0 FF FF 7F F0 FF FF 7F  do1..U..........
0110: 66 64 6F 31 46 00 66 09  80 F8 FF FF 7F F8 FF FF  fdo1F.f.........
0120: 7F 70 6F 69 32 55 06 80  F0 FF FF 7F F0 FF FF 7F  .poi2U..........
0130: 66 64 69 31 45 06 80 F0  FF FF 7F F0 FF FF 7F 66  fdi1E..........f
0140: 64 69 31 04 80 53 F8 FF  FF 7F F8 FF FF 7F 74 6C  di1..S........tl
0150: 6B 30 03 01 10 0B 80 01  81 01 02 00 10 0C 80 00  k0..............
0160: 81 01 66 00 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  ..f..........tlk
0170: 30 1D 0D 80 23 1D 0E 80  23 03 01 10 0B 80 01 81  0...#...#.......
0180: 01 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x001D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0022 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0023 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0024 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  4: 0x0033 [0x1D] PRINT_EVENT_MESSAGE(message_id=6853*)
    → "Hello, therrre. I don't believe I've seen you before. You must be new in town."
  5: 0x0036 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0037 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x003C [0x24] CREATE_DIALOG(message_id=6848*, default_option=0*, option_flags=0*)
    → "Are you new to Mhaura? [Yes, it's my first time here./No, I've come here plenty of times.]"
  8: 0x0043 [0x25] WAIT_DIALOG_SELECT()
  9: 0x0044 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x015A
 10: 0x004C [0x42] SET_CLI_EVENT_CANCEL_DATA()
 11: 0x004D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
 12: 0x005C [0x1D] PRINT_EVENT_MESSAGE(message_id=6854*)
    → "I thought so. Welcome to Mhaura! Visitors like you should go to the governor's house to get an orientation."
 13: 0x005F [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0060 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
 15: 0x006D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 16: 0x007E [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 17: 0x008D [0x46] CAMERA_CONTROL: Disable user control
 18: 0x008F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "se07" with entities [LocalPlayer, LocalPlayer], work=[149*, 0*]
 19: 0x00A0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x00B1 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 21: 0x00C0 [0x39] SET_ENTITY_DIRECTION(direction=10.7°*)
 22: 0x00C3 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 23: 0x00C4 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 24: 0x00C5 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi1" with entities [EventEntity, EventEntity], work=52*
 25: 0x00D4 [0x1D] PRINT_EVENT_MESSAGE(message_id=6855*)
    → "Go up the stairs at the western end of this square, then up again the stairrrs on your left. Good luck!"
 26: 0x00D7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x00D8 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "se07" with entities [LocalPlayer, LocalPlayer], work=149*
 28: 0x00E7 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi1" with entities [EventEntity, EventEntity]
 29: 0x00F4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 30: 0x0105 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 31: 0x0114 [0x46] CAMERA_CONTROL: Restore default settings
 32: 0x0116 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi2" with entities [EventEntity, EventEntity], work=52*
 33: 0x0125 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 34: 0x0134 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 35: 0x0145 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
 36: 0x0152 [0x03] Work_Zone[1] = 2*
 37: 0x0157 [0x01] GOTO 0x0181
 38: 0x015A [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0181
 39: 0x0162 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
 40: 0x0171 [0x1D] PRINT_EVENT_MESSAGE(message_id=6856*)
    → "Rrreally? I'm sorry. I'm usually good with names..."
 41: 0x0174 [0x23] WAIT_FOR_DIALOG_INTERACTION
 42: 0x0175 [0x1D] PRINT_EVENT_MESSAGE(message_id=6857*)
    → "You should visit the governor's house if you haven't already. They will answer any questions you have about Mhaura."
 43: 0x0178 [0x23] WAIT_FOR_DIALOG_INTERACTION
 44: 0x0179 [0x03] Work_Zone[1] = 2*
 45: 0x017E [0x01] GOTO 0x0181

SUBROUTINE_0181:
 46: 0x0181 [0x21] END_EVENT
 47: 0x0182 [0x00] END_REQSTACK()
```
