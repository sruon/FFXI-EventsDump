# 17797123 - Somo Aatsula

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Mhaura (ID: 249) |
| Block Size       | 544 bytes        |
| Total Events     | 4                |
| References Count | 18               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [35](#event-35)       | 0x0001       |    381 |             51 |
| [36](#event-36)       | 0x017E       |     28 |              8 |
| [37](#event-37)       | 0x019A       |     28 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0032      |          50 |
|       1 | 0x1ABF      |        6847 |
|       2 | 0x1AC0      |        6848 |
|       3 | 0x0000      |           0 |
|       4 | 0x1AC1      |        6849 |
|       5 | 0x00C8      |         200 |
|       6 | 0x0095      |         149 |
|       7 | 0x05C5      |        1477 |
|       8 | 0x0034      |          52 |
|       9 | 0x1AC2      |        6850 |
|      10 | 0x0002      |           2 |
|      11 | 0x0001      |           1 |
|      12 | 0x0033      |          51 |
|      13 | 0x1AC3      |        6851 |
|      14 | 0x003C      |          60 |
|      15 | 0x1AC4      |        6852 |
|      16 | 0x1BCA      |        7114 |
|      17 | 0x1BCB      |        7115 |

## String References

- **6847**: Hello. I haven't seen you around here beforrre. Are you new in town?
- **6848**: Are you new to Mhaura? [Yes, it's my first time here./No, I've come here plenty of times.]
- **6849**: Ah, I thought so. Welcome to Mhaura. You should go to the governor's house. They'll tell you all you need to know about our little town.
- **6850**: First, climb the stairs there, and walk along the ledge to another set of stairs. Go up, and you're therrre.
- **6851**: You're not pulling my tail, are you? Hmm...I guess I must've just missed you. Still, you look lost.
- **6852**: Have you been to the governor's house yet? If not, you should. They'll tell you all you need to know about our little town.
- **7114**: I can't let you through this door. This is the guards' barrrracks. No unauthorized people allowed.
- **7115**: You can't tell if you're in the town, but I hearrr the beastmen are up to something out there. How are things where you come from?

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

### Event 35

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 381 bytes |
| Instructions | 51        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 5E 69 64 6C 30  ...tlk0...#^idl0
0020: 24 02 80 03 80 03 80 25  02 00 10 03 80 00 36 01  $......%......6.
0030: 42 66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30  Bf..........tlk0
0040: 1D 04 80 23 5E 69 64 6C  30 45 05 80 F0 FF FF 7F  ...#^idl0E......
0050: F0 FF FF 7F 66 64 6F 31  03 80 55 05 80 F0 FF FF  ....fdo1..U.....
0060: 7F F0 FF FF 7F 66 64 6F  31 46 01 45 06 80 F0 FF  .....fdo1F.E....
0070: FF 7F F0 FF FF 7F 73 65  30 36 03 80 45 05 80 F0  ......se06..E...
0080: FF FF 7F F0 FF FF 7F 66  64 69 31 03 80 55 05 80  .......fdi1..U..
0090: F0 FF FF 7F F0 FF FF 7F  66 64 69 31 39 07 80 6F  ........fdi19..o
00A0: 70 66 08 80 F8 FF FF 7F  F8 FF FF 7F 70 6F 69 31  pf..........poi1
00B0: 1D 09 80 23 55 06 80 F0  FF FF 7F F0 FF FF 7F 73  ...#U..........s
00C0: 65 30 36 53 F8 FF FF 7F  F8 FF FF 7F 70 6F 69 31  e06S........poi1
00D0: 45 05 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 31 03  E..........fdo1.
00E0: 80 55 05 80 F0 FF FF 7F  F0 FF FF 7F 66 64 6F 31  .U..........fdo1
00F0: 46 00 66 08 80 F8 FF FF  7F F8 FF FF 7F 70 6F 69  F.f..........poi
0100: 32 55 05 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 31  2U..........fdi1
0110: 45 05 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 31 03  E..........fdi1.
0120: 80 53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 03 01  .S........tlk0..
0130: 10 0A 80 01 7C 01 02 00  10 0B 80 00 7C 01 66 0C  ....|.......|.f.
0140: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 1D 0D 80  .........tlk0...
0150: 23 53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1C 0E  #S........tlk0..
0160: 80 66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30  .f..........tlk0
0170: 1D 0F 80 23 03 01 10 0A  80 01 7C 01 21 00        ...#......|.!.  
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=6847*)
    → "Hello. I haven't seen you around here beforrre. Are you new in town?"
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x0020 [0x24] CREATE_DIALOG(message_id=6848*, default_option=0*, option_flags=0*)
    → "Are you new to Mhaura? [Yes, it's my first time here./No, I've come here plenty of times.]"
  8: 0x0027 [0x25] WAIT_DIALOG_SELECT()
  9: 0x0028 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0136
 10: 0x0030 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 11: 0x0031 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
 12: 0x0040 [0x1D] PRINT_EVENT_MESSAGE(message_id=6849*)
    → "Ah, I thought so. Welcome to Mhaura. You should go to the governor's house. They'll tell you all you need to know about our little town."
 13: 0x0043 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0044 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 15: 0x0049 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 16: 0x005A [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 17: 0x0069 [0x46] CAMERA_CONTROL: Disable user control
 18: 0x006B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "se06" with entities [LocalPlayer, LocalPlayer], work=[149*, 0*]
 19: 0x007C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x008D [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 21: 0x009C [0x39] SET_ENTITY_DIRECTION(direction=8.1°*)
 22: 0x009F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 23: 0x00A0 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 24: 0x00A1 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi1" with entities [EventEntity, EventEntity], work=52*
 25: 0x00B0 [0x1D] PRINT_EVENT_MESSAGE(message_id=6850*)
    → "First, climb the stairs there, and walk along the ledge to another set of stairs. Go up, and you're therrre."
 26: 0x00B3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x00B4 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "se06" with entities [LocalPlayer, LocalPlayer], work=149*
 28: 0x00C3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi1" with entities [EventEntity, EventEntity]
 29: 0x00D0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 30: 0x00E1 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 31: 0x00F0 [0x46] CAMERA_CONTROL: Restore default settings
 32: 0x00F2 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi2" with entities [EventEntity, EventEntity], work=52*
 33: 0x0101 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 34: 0x0110 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 35: 0x0121 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
 36: 0x012E [0x03] Work_Zone[1] = 2*
 37: 0x0133 [0x01] GOTO 0x017C
 38: 0x0136 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x017C
 39: 0x013E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=51*
 40: 0x014D [0x1D] PRINT_EVENT_MESSAGE(message_id=6851*)
    → "You're not pulling my tail, are you? Hmm...I guess I must've just missed you. Still, you look lost."
 41: 0x0150 [0x23] WAIT_FOR_DIALOG_INTERACTION
 42: 0x0151 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
 43: 0x015E [0x1C] WAIT(60* ticks)
 44: 0x0161 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
 45: 0x0170 [0x1D] PRINT_EVENT_MESSAGE(message_id=6852*)
    → "Have you been to the governor's house yet? If not, you should. They'll tell you all you need to know about our little town."
 46: 0x0173 [0x23] WAIT_FOR_DIALOG_INTERACTION
 47: 0x0174 [0x03] Work_Zone[1] = 2*
 48: 0x0179 [0x01] GOTO 0x017C

SUBROUTINE_017C:
 49: 0x017C [0x21] END_EVENT
 50: 0x017D [0x00] END_REQSTACK()
```

### Event 36

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x017E   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                            1E F0                ..
0180: FF FF 7F 6F 70 66 00 80  F8 FF FF 7F F8 FF FF 7F  ...opf..........
0190: 74 6C 6B 30 1D 10 80 23  21 00                    tlk0...#!.      
```

#### Opcodes

```
  0: 0x017E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0183 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0184 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0185 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  4: 0x0194 [0x1D] PRINT_EVENT_MESSAGE(message_id=7114*)
    → "I can't let you through this door. This is the guards' barrrracks. No unauthorized people allowed."
  5: 0x0197 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0198 [0x21] END_EVENT
  7: 0x0199 [0x00] END_REQSTACK()
```

### Event 37

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x019A   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                                1E F0 FF FF 7F 6F            .....o
01A0: 70 66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30  pf..........tlk0
01B0: 1D 11 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x019A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x019F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x01A0 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x01A1 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  4: 0x01B0 [0x1D] PRINT_EVENT_MESSAGE(message_id=7115*)
    → "You can't tell if you're in the town, but I hearrr the beastmen are up to something out there. How are things where you come from?"
  5: 0x01B3 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x01B4 [0x21] END_EVENT
  7: 0x01B5 [0x00] END_REQSTACK()
```
