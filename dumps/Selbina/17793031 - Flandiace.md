# 17793031 - Flandiace

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Selbina (ID: 248) |
| Block Size       | 476 bytes         |
| Total Events     | 3                 |
| References Count | 18                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [12](#event-12)       | 0x0001       |    285 |             41 |
| [13](#event-13)       | 0x011E       |     89 |             23 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x1A20      |        6688 |
|       2 | 0x1A21      |        6689 |
|       3 | 0x0000      |           0 |
|       4 | 0x1A22      |        6690 |
|       5 | 0x00C8      |         200 |
|       6 | 0x003C      |          60 |
|       7 | 0x0094      |         148 |
|       8 | 0x1A23      |        6691 |
|       9 | 0x0001      |           1 |
|      10 | 0x1A24      |        6692 |
|      11 | 0x1A25      |        6693 |
|      12 | 0x0002      |           2 |
|      13 | 0x0003      |           3 |
|      14 | 0x1B5A      |        7002 |
|      15 | 0x1B5B      |        7003 |
|      16 | 0x1B5C      |        7004 |
|      17 | 0x1B5D      |        7005 |

## String References

- **6688**: Hello there. Is this your first visit to our fine town?
- **6689**: Well, is it? [Why, yes./No, I come here all the time.]
- **6690**: Yes, I thought as much. You'd best head to the mayor's office.
- **6691**: Trot down towards the shore and take the first stairway. Turn right, follow the wall, and there it will be.
- **6692**: Is that a fact? I never forget a face. Oh well. Never mind.
- **6693**: Have you been to see the mayor? If not, you should!
- **7002**: Our village may be small, but so many stop here to rest on the road between Bastok and San d'Oria.
- **7003**: Sorry, the station is for militia personnel only.
- **7004**: If you're heading outside, remember that there's safety in numbers. Gather people of different talents to cover any weaknesses.
- **7005**: If you're here for the ship, the docks are straight down the stairs from here.

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

### Event 12

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 285 bytes |
| Instructions | 41        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 5E 69 64 6C 30  ...tlk0...#^idl0
0020: 24 02 80 03 80 03 80 25  02 00 10 03 80 00 F5 00  $......%........
0030: 42 66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30  Bf..........tlk0
0040: 1D 04 80 23 45 05 80 F0  FF FF 7F F0 FF FF 7F 66  ...#E..........f
0050: 64 6F 31 03 80 55 05 80  F0 FF FF 7F F0 FF FF 7F  do1..U..........
0060: 66 64 6F 31 46 01 1C 06  80 45 07 80 F0 FF FF 7F  fdo1F....E......
0070: F0 FF FF 7F 73 65 30 32  03 80 45 05 80 F0 FF FF  ....se02..E.....
0080: 7F F0 FF FF 7F 66 64 69  31 03 80 55 05 80 F0 FF  .....fdi1..U....
0090: FF 7F F0 FF FF 7F 66 64  69 31 1D 08 80 23 55 07  ......fdi1...#U.
00A0: 80 F0 FF FF 7F F0 FF FF  7F 73 65 30 32 45 05 80  .........se02E..
00B0: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 03 80 55 05  ........fdo1..U.
00C0: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 1C 06 80  .........fdo1...
00D0: 46 00 55 05 80 F0 FF FF  7F F0 FF FF 7F 66 64 69  F.U..........fdi
00E0: 31 45 05 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 31  1E..........fdi1
00F0: 03 80 01 17 01 02 00 10  09 80 00 17 01 66 00 80  .............f..
0100: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 1D 0A 80 23  ........tlk0...#
0110: 1D 0B 80 23 01 17 01 03  01 10 0C 80 21 00        ...#........!.  
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=6688*)
    → "Hello there. Is this your first visit to our fine town?"
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x0020 [0x24] CREATE_DIALOG(message_id=6689*, default_option=0*, option_flags=0*)
    → "Well, is it? [Why, yes./No, I come here all the time.]"
  8: 0x0027 [0x25] WAIT_DIALOG_SELECT()
  9: 0x0028 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00F5
 10: 0x0030 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 11: 0x0031 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
 12: 0x0040 [0x1D] PRINT_EVENT_MESSAGE(message_id=6690*)
    → "Yes, I thought as much. You'd best head to the mayor's office."
 13: 0x0043 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0044 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 15: 0x0055 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 16: 0x0064 [0x46] CAMERA_CONTROL: Disable user control
 17: 0x0066 [0x1C] WAIT(60* ticks)
 18: 0x0069 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "se02" with entities [LocalPlayer, LocalPlayer], work=[148*, 0*]
 19: 0x007A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x008B [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 21: 0x009A [0x1D] PRINT_EVENT_MESSAGE(message_id=6691*)
    → "Trot down towards the shore and take the first stairway. Turn right, follow the wall, and there it will be."
 22: 0x009D [0x23] WAIT_FOR_DIALOG_INTERACTION
 23: 0x009E [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "se02" with entities [LocalPlayer, LocalPlayer], work=148*
 24: 0x00AD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 25: 0x00BE [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 26: 0x00CD [0x1C] WAIT(60* ticks)
 27: 0x00D0 [0x46] CAMERA_CONTROL: Restore default settings
 28: 0x00D2 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 29: 0x00E1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 30: 0x00F2 [0x01] GOTO 0x0117
 31: 0x00F5 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0117
 32: 0x00FD [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
 33: 0x010C [0x1D] PRINT_EVENT_MESSAGE(message_id=6692*)
    → "Is that a fact? I never forget a face. Oh well. Never mind."
 34: 0x010F [0x23] WAIT_FOR_DIALOG_INTERACTION
 35: 0x0110 [0x1D] PRINT_EVENT_MESSAGE(message_id=6693*)
    → "Have you been to see the mayor? If not, you should!"
 36: 0x0113 [0x23] WAIT_FOR_DIALOG_INTERACTION
 37: 0x0114 [0x01] GOTO 0x0117

SUBROUTINE_0117:
 38: 0x0117 [0x03] Work_Zone[1] = 2*
 39: 0x011C [0x21] END_EVENT
 40: 0x011D [0x00] END_REQSTACK()
```

### Event 13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x011E   |
| Data Size    | 89 bytes |
| Instructions | 23       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                            1E F0                ..
0120: FF FF 7F 13 00 00 0D 80  6F 70 66 00 80 F8 FF FF  ........opf.....
0130: 7F F8 FF FF 7F 74 6C 6B  30 02 00 00 03 80 80 48  .....tlk0......H
0140: 01 1D 0E 80 23 01 75 01  02 00 00 09 80 80 57 01  ....#.u.......W.
0150: 1D 0F 80 23 01 75 01 02  00 00 0C 80 80 66 01 1D  ...#.u.......f..
0160: 10 80 23 01 75 01 02 00  00 0D 80 80 75 01 1D 11  ..#.u.......u...
0170: 80 23 01 75 01 21 00                              .#.u.!.         
```

#### Opcodes

```
  0: 0x011E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0123 [0x13] ExtData[1]->WorkLocal[0] = rand() % 3*
  2: 0x0128 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0129 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x012A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  5: 0x0139 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x0148
  6: 0x0141 [0x1D] PRINT_EVENT_MESSAGE(message_id=7002*)
    → "Our village may be small, but so many stop here to rest on the road between Bastok and San d'Oria."
  7: 0x0144 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0145 [0x01] GOTO 0x0175
  9: 0x0148 [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x0157
 10: 0x0150 [0x1D] PRINT_EVENT_MESSAGE(message_id=7003*)
    → "Sorry, the station is for militia personnel only."
 11: 0x0153 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0154 [0x01] GOTO 0x0175
 13: 0x0157 [0x02] IF !(ExtData[1]->WorkLocal[0] == 2*) GOTO 0x0166
 14: 0x015F [0x1D] PRINT_EVENT_MESSAGE(message_id=7004*)
    → "If you're heading outside, remember that there's safety in numbers. Gather people of different talents to cover any weaknesses."
 15: 0x0162 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0163 [0x01] GOTO 0x0175
 17: 0x0166 [0x02] IF !(ExtData[1]->WorkLocal[0] == 3*) GOTO 0x0175
 18: 0x016E [0x1D] PRINT_EVENT_MESSAGE(message_id=7005*)
    → "If you're here for the ship, the docks are straight down the stairs from here."
 19: 0x0171 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x0172 [0x01] GOTO 0x0175

SUBROUTINE_0175:
 21: 0x0175 [0x21] END_EVENT
 22: 0x0176 [0x00] END_REQSTACK()
```
