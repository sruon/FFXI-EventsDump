# 16814515 - Stone Door

## Common Data

| Field            | Value           |
|------------------|-----------------|
| Zone             | Pso'Xja (ID: 9) |
| Block Size       | 456 bytes       |
| Total Events     | 3               |
| References Count | 11              |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [69](#event-69)       | 0x0001       |    193 |             35 |
| [70](#event-70)       | 0x00C2       |    189 |             33 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1C62      |        7266 |
|       1 | 0x1C68      |        7272 |
|       2 | 0x0001      |           1 |
|       3 | 0x0000      |           0 |
|       4 | 0x00C8      |         200 |
|       5 | 0x003C      |          60 |
|       6 | 0x0012      |          18 |
|       7 | 0x00A0      |         160 |
|       8 | 0x00B4      |         180 |
|       9 | 0x0096      |         150 |
|      10 | 0x1C69      |        7273 |

## String References

- **7266**: The trap on the door is broken.
- **7272**: Enter through the door? [Yes./No.]
- **7273**: Exit through the door? [Yes./No.]

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

### Event 69

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 193 bytes |
| Instructions | 35        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 48 00 80 23 24  01 80 02 80 03 80 25 02    .H..#$......%.
0010: 00 10 03 80 00 B3 00 43  00 43 01 46 01 42 45 04  .......C.C.F.BE.
0020: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 03 80 1C  .........fdo1...
0030: 05 80 38 06 80 45 07 80  F0 FF FF 7F F0 FF FF 7F  ..8..E..........
0040: 39 76 7A 31 03 80 29 01  F0 FF FF 7F 31 29 01 F0  9vz1..).....1)..
0050: FF FF 7F 30 45 04 80 F0  FF FF 7F F0 FF FF 7F 66  ...0E..........f
0060: 64 69 31 03 80 1C 05 80  4C 1C 08 80 27 01 F0 FF  di1.....L...'...
0070: FF 7F 32 1C 08 80 4D 1C  09 80 45 04 80 F0 FF FF  ..2...M...E.....
0080: 7F F0 FF FF 7F 66 64 6F  31 03 80 1C 05 80 52 07  .....fdo1.....R.
0090: 80 F0 FF FF 7F F0 FF FF  7F 39 76 7A 31 45 04 80  .........9vz1E..
00A0: F0 FF FF 7F F0 FF FF 7F  66 64 69 31 03 80 46 00  ........fdi1..F.
00B0: 01 BE 00 02 00 10 02 80  00 BE 00 01 BE 00 20 00  .............. .
00C0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x48] [System] [7266*]:
    → "The trap on the door is broken."
  2: 0x0006 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0007 [0x24] CREATE_DIALOG(message_id=7272*, default_option=1*, option_flags=0*)
    → "Enter through the door? [Yes./No.]"
  4: 0x000E [0x25] WAIT_DIALOG_SELECT()
  5: 0x000F [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00B3
  6: 0x0017 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  7: 0x0019 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  8: 0x001B [0x46] CAMERA_CONTROL: Disable user control
  9: 0x001D [0x42] SET_CLI_EVENT_CANCEL_DATA()
 10: 0x001E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 11: 0x002F [0x1C] WAIT(60* ticks)
 12: 0x0032 [0x38] SET_CLIENT_EVENT_MODE(mode=18*)
 13: 0x0035 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "9vz1" with entities [LocalPlayer, LocalPlayer], work=[160*, 0*]
 14: 0x0046 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x31)
 15: 0x004D [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x30)
 16: 0x0054 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 17: 0x0065 [0x1C] WAIT(60* ticks)
 18: 0x0068 [0x4C] EventEntity->StatusEvent = 8 // Open door
 19: 0x0069 [0x1C] WAIT(180* ticks)
 20: 0x006C [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x32)
 21: 0x0073 [0x1C] WAIT(180* ticks)
 22: 0x0076 [0x4D] EventEntity->StatusEvent = 9 // Close door
 23: 0x0077 [0x1C] WAIT(150* ticks)
 24: 0x007A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 25: 0x008B [0x1C] WAIT(60* ticks)
 26: 0x008E [0x52] END_LOAD_SCHEDULER: End scheduler "9vz1" with entities [LocalPlayer, LocalPlayer], work=160*
 27: 0x009D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 28: 0x00AE [0x46] CAMERA_CONTROL: Restore default settings
 29: 0x00B0 [0x01] GOTO 0x00BE
 30: 0x00B3 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00BE
 31: 0x00BB [0x01] GOTO 0x00BE

SUBROUTINE_00BE:
 32: 0x00BE [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 33: 0x00C0 [0x21] END_EVENT
 34: 0x00C1 [0x00] END_REQSTACK()
```

### Event 70

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00C2    |
| Data Size    | 189 bytes |
| Instructions | 33        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:       20 01 24 0A 80 02  80 03 80 25 02 00 10 03     .$......%....
00D0: 80 00 70 01 43 00 43 01  46 01 42 45 04 80 F0 FF  ..p.C.C.F.BE....
00E0: FF 7F F0 FF FF 7F 66 64  6F 31 03 80 1C 05 80 38  ......fdo1.....8
00F0: 06 80 45 07 80 F0 FF FF  7F F0 FF FF 7F 39 76 7A  ..E..........9vz
0100: 32 03 80 29 01 F0 FF FF  7F 34 29 01 F0 FF FF 7F  2..).....4).....
0110: 33 45 04 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 31  3E..........fdi1
0120: 03 80 1C 05 80 4C 1C 08  80 27 01 F0 FF FF 7F 35  .....L...'.....5
0130: 1C 08 80 4D 1C 09 80 45  04 80 F0 FF FF 7F F0 FF  ...M...E........
0140: FF 7F 66 64 6F 31 03 80  1C 05 80 52 07 80 F0 FF  ..fdo1.....R....
0150: FF 7F F0 FF FF 7F 39 76  7A 32 45 04 80 F0 FF FF  ......9vz2E.....
0160: 7F F0 FF FF 7F 66 64 69  31 03 80 46 00 01 7B 01  .....fdi1..F..{.
0170: 02 00 10 02 80 00 7B 01  01 7B 01 20 00 21 00     ......{..{. .!. 
```

#### Opcodes

```
  0: 0x00C2 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x00C4 [0x24] CREATE_DIALOG(message_id=7273*, default_option=1*, option_flags=0*)
    → "Exit through the door? [Yes./No.]"
  2: 0x00CB [0x25] WAIT_DIALOG_SELECT()
  3: 0x00CC [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0170
  4: 0x00D4 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  5: 0x00D6 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  6: 0x00D8 [0x46] CAMERA_CONTROL: Disable user control
  7: 0x00DA [0x42] SET_CLI_EVENT_CANCEL_DATA()
  8: 0x00DB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  9: 0x00EC [0x1C] WAIT(60* ticks)
 10: 0x00EF [0x38] SET_CLIENT_EVENT_MODE(mode=18*)
 11: 0x00F2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "9vz2" with entities [LocalPlayer, LocalPlayer], work=[160*, 0*]
 12: 0x0103 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x34)
 13: 0x010A [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x33)
 14: 0x0111 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 15: 0x0122 [0x1C] WAIT(60* ticks)
 16: 0x0125 [0x4C] EventEntity->StatusEvent = 8 // Open door
 17: 0x0126 [0x1C] WAIT(180* ticks)
 18: 0x0129 [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x35)
 19: 0x0130 [0x1C] WAIT(180* ticks)
 20: 0x0133 [0x4D] EventEntity->StatusEvent = 9 // Close door
 21: 0x0134 [0x1C] WAIT(150* ticks)
 22: 0x0137 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 23: 0x0148 [0x1C] WAIT(60* ticks)
 24: 0x014B [0x52] END_LOAD_SCHEDULER: End scheduler "9vz2" with entities [LocalPlayer, LocalPlayer], work=160*
 25: 0x015A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 26: 0x016B [0x46] CAMERA_CONTROL: Restore default settings
 27: 0x016D [0x01] GOTO 0x017B
 28: 0x0170 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x017B
 29: 0x0178 [0x01] GOTO 0x017B

SUBROUTINE_017B:
 30: 0x017B [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 31: 0x017D [0x21] END_EVENT
 32: 0x017E [0x00] END_REQSTACK()
```
