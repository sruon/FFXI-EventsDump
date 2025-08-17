# 17531163 - Cermet Door

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Lower Delkfutt's Tower (ID: 184) |
| Block Size       | 688 bytes                        |
| Total Events     | 5                                |
| References Count | 16                               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [1](#event-1)            | 0x0001       |    564 |             71 |
| [12](#event-12)          | 0x0235       |     17 |             10 |
| [65535.1](#event-655351) | 0x0246       |      2 |              2 |
| [65535.2](#event-655352) | 0x0248       |      2 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x0013      |          19 |
|       3 | 0x0092      |         146 |
|       4 | 0x001E      |          30 |
|       5 | 0x0078      |         120 |
|       6 | 0x003C      |          60 |
|       7 | 0x005A      |          90 |
|       8 | 0x00A9      |         169 |
|       9 | 0x00AA      |         170 |
|      10 | 0x00AB      |         171 |
|      11 | 0x00AC      |         172 |
|      12 | 0x00AD      |         173 |
|      13 | 0x00AE      |         174 |
|      14 | 0x0096      |         150 |
|      15 | 0x00A1      |         161 |

## String References

- **161**: You see nothing of particular interest.

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

### Event 1

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 564 bytes |
| Instructions | 71        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 46 01 42 45 00  80 F0 FF FF 7F F0 FF FF    .F.BE.........
0010: 7F 66 64 6F 31 01 80 55  00 80 F0 FF FF 7F F0 FF  .fdo1..U........
0020: FF 7F 66 64 6F 31 38 02  80 29 03 F0 FF FF 7F 13  ..fdo18..)......
0030: 45 03 80 F0 FF FF 7F F0  FF FF 7F 63 6D 34 32 01  E..........cm42.
0040: 80 55 03 80 F0 FF FF 7F  F0 FF FF 7F 63 6D 34 32  .U..........cm42
0050: 1C 04 80 45 00 80 F0 FF  FF 7F F0 FF FF 7F 66 64  ...E..........fd
0060: 69 31 01 80 55 00 80 F0  FF FF 7F F0 FF FF 7F 66  i1..U..........f
0070: 64 69 31 4C 4E 00 1C 81  0B 01 1C 05 80 2C 1C 81  di1LN........,..
0080: 0B 01 1C 81 0B 01 63 6F  72 70 53 1C 81 0B 01 1C  ......corpS.....
0090: 81 0B 01 63 6F 72 70 29  03 F0 FF FF 7F 14 4A F0  ...corp)......J.
00A0: FF FF 7F 1C 81 0B 01 1C  04 80 45 03 80 F0 FF FF  ..........E.....
00B0: 7F F0 FF FF 7F 63 6D 34  33 01 80 55 03 80 F0 FF  .....cm43..U....
00C0: FF 7F F0 FF FF 7F 63 6D  34 33 6F 76 F0 FF FF 7F  ......cm43ov....
00D0: 29 03 F0 FF FF 7F 15 1C  06 80 2C F0 FF FF 7F F0  ).........,.....
00E0: FF FF 7F 72 65 73 30 1C  06 80 45 00 80 F0 FF FF  ...res0...E.....
00F0: 7F F0 FF FF 7F 66 64 6F  31 01 80 55 00 80 F0 FF  .....fdo1..U....
0100: FF 7F F0 FF FF 7F 66 64  6F 31 45 03 80 F0 FF FF  ......fdo1E.....
0110: 7F F0 FF FF 7F 63 6D 34  62 01 80 55 03 80 F0 FF  .....cm4b..U....
0120: FF 7F F0 FF FF 7F 63 6D  34 62 2C F0 FF FF 7F F0  ......cm4b,.....
0130: FF FF 7F 72 65 73 32 4A  1C 81 0B 01 F0 FF FF 7F  ...res2J........
0140: 6F 76 1C 81 0B 01 27 04  1C 81 0B 01 06 1C 07 80  ov....'.........
0150: 45 00 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 32 01  E..........fdi2.
0160: 80 55 00 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 32  .U..........fdi2
0170: 2B 1C 81 0B 01 08 80 23  45 03 80 F0 FF FF 7F F0  +......#E.......
0180: FF FF 7F 63 6D 34 37 01  80 29 05 1C 81 0B 01 07  ...cm47..)......
0190: 2B 1C 81 0B 01 09 80 23  27 03 1C 81 0B 01 04 2B  +......#'......+
01A0: 1C 81 0B 01 0A 80 23 29  04 1C 81 0B 01 05 2B 1C  ......#)......+.
01B0: 81 0B 01 0B 80 23 27 03  1C 81 0B 01 03 2B 1C 81  .....#'......+..
01C0: 0B 01 0C 80 23 2B 1C 81  0B 01 0D 80 23 29 04 1C  ....#+......#)..
01D0: 81 0B 01 08 27 05 1C 81  0B 01 02 45 03 80 F0 FF  ....'......E....
01E0: FF 7F F0 FF FF 7F 63 6D  34 65 01 80 1C 06 80 27  ......cm4e.....'
01F0: 05 F0 FF FF 7F 16 45 00  80 F0 FF FF 7F F0 FF FF  ......E.........
0200: 7F 66 64 6F 32 01 80 55  00 80 F0 FF FF 7F F0 FF  .fdo2..U........
0210: FF 7F 66 64 6F 32 4E 01  1C 81 0B 01 4D 1C 0E 80  ..fdo2N.....M...
0220: 46 00 45 00 80 F0 FF FF  7F F0 FF FF 7F 66 64 69  F.E..........fdi
0230: 32 01 80 21 00                                    2..!.           
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x46] CAMERA_CONTROL: Disable user control
  2: 0x0005 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  3: 0x0006 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x0017 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
  5: 0x0026 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  6: 0x0029 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=LocalPlayer, tag_num=0x13)
  7: 0x0030 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm42" with entities [LocalPlayer, LocalPlayer], work=[146*, 0*]
  8: 0x0041 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "cm42" with entities [LocalPlayer, LocalPlayer], work=146*
  9: 0x0050 [0x1C] WAIT(30* ticks)
 10: 0x0053 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 11: 0x0064 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 12: 0x0073 [0x4C] EventEntity->StatusEvent = 8 // Open door
 13: 0x0074 [0x4E] SET_ENTITY_HIDE_FLAG: Show Altair (ID: 17531164/0x010B811C)
 14: 0x007A [0x1C] WAIT(120* ticks)
 15: 0x007D [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "corp" with entities [Altair (ID: 17531164/0x010B811C), Altair (ID: 17531164/0x010B811C)]
 16: 0x008A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "corp" with entities [Altair (ID: 17531164/0x010B811C), Altair (ID: 17531164/0x010B811C)]
 17: 0x0097 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=LocalPlayer, tag_num=0x14)
 18: 0x009E [0x4A] LocalPlayer looks at Altair (ID: 17531164/0x010B811C)
 19: 0x00A7 [0x1C] WAIT(30* ticks)
 20: 0x00AA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm43" with entities [LocalPlayer, LocalPlayer], work=[146*, 0*]
 21: 0x00BB [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "cm43" with entities [LocalPlayer, LocalPlayer], work=146*
 22: 0x00CA [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 23: 0x00CB [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
 24: 0x00D0 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=LocalPlayer, tag_num=0x15)
 25: 0x00D7 [0x1C] WAIT(60* ticks)
 26: 0x00DA [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "res0" with entities [LocalPlayer, LocalPlayer]
 27: 0x00E7 [0x1C] WAIT(60* ticks)
 28: 0x00EA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 29: 0x00FB [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 30: 0x010A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm4b" with entities [LocalPlayer, LocalPlayer], work=[146*, 0*]
 31: 0x011B [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "cm4b" with entities [LocalPlayer, LocalPlayer], work=146*
 32: 0x012A [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "res2" with entities [LocalPlayer, LocalPlayer]
 33: 0x0137 [0x4A] Altair (ID: 17531164/0x010B811C) looks at LocalPlayer
 34: 0x0140 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 35: 0x0141 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Altair (ID: 17531164/0x010B811C) Render.Flags0 and Render.Flags3 conditions are met
 36: 0x0146 [0x27] REQ_SET(priority=0x04, entity_id=Altair (ID: 17531164/0x010B811C), tag_num=0x06)
 37: 0x014D [0x1C] WAIT(90* ticks)
 38: 0x0150 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 39: 0x0161 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=200*
 40: 0x0170 [0x2B] Altair (ID: 17531164/0x010B811C) [169*]:
    → "Un... Ungh..."
 41: 0x0177 [0x23] WAIT_FOR_DIALOG_INTERACTION
 42: 0x0178 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm47" with entities [LocalPlayer, LocalPlayer], work=[146*, 0*]
 43: 0x0189 [0x29] REQ_SET_WAIT(priority=0x05, entity_id=Altair (ID: 17531164/0x010B811C), tag_num=0x07)
 44: 0x0190 [0x2B] Altair (ID: 17531164/0x010B811C) [170*]:
    → "Who are you? Not an enemy, at any rate. I'm glad you found me. I am ambassador Altair from Bastok."
 45: 0x0197 [0x23] WAIT_FOR_DIALOG_INTERACTION
 46: 0x0198 [0x27] REQ_SET(priority=0x03, entity_id=Altair (ID: 17531164/0x010B811C), tag_num=0x04)
 47: 0x019F [0x2B] Altair (ID: 17531164/0x010B811C) [171*]:
    → "What? You were sent on a mission for the embassy...? I see. My apologies...if it weren't for me, you wouldn't have had to come to such a dangerous place."
 48: 0x01A6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 49: 0x01A7 [0x29] REQ_SET_WAIT(priority=0x04, entity_id=Altair (ID: 17531164/0x010B811C), tag_num=0x05)
 50: 0x01AE [0x2B] Altair (ID: 17531164/0x010B811C) [172*]:
    → "I should never have let my guard down...I was struck from behind, and the next thing I knew, I woke up here. I shudder to think at what would have happened to me if you hadn't come."
 51: 0x01B5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 52: 0x01B6 [0x27] REQ_SET(priority=0x03, entity_id=Altair (ID: 17531164/0x010B811C), tag_num=0x03)
 53: 0x01BD [0x2B] Altair (ID: 17531164/0x010B811C) [173*]:
    → "This place is dangerous...but not only because of the monsters. I sense something more ominous in the air..."
 54: 0x01C4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 55: 0x01C5 [0x2B] Altair (ID: 17531164/0x010B811C) [174*]:
    → "In any case, we should get out of here as soon as possible. I can find my way out. Come meet me at the embassy when you can."
 56: 0x01CC [0x23] WAIT_FOR_DIALOG_INTERACTION
 57: 0x01CD [0x29] REQ_SET_WAIT(priority=0x04, entity_id=Altair (ID: 17531164/0x010B811C), tag_num=0x08)
 58: 0x01D4 [0x27] REQ_SET(priority=0x05, entity_id=Altair (ID: 17531164/0x010B811C), tag_num=0x02)
 59: 0x01DB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm4e" with entities [LocalPlayer, LocalPlayer], work=[146*, 0*]
 60: 0x01EC [0x1C] WAIT(60* ticks)
 61: 0x01EF [0x27] REQ_SET(priority=0x05, entity_id=LocalPlayer, tag_num=0x16)
 62: 0x01F6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 63: 0x0207 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=200*
 64: 0x0216 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Altair (ID: 17531164/0x010B811C)
 65: 0x021C [0x4D] EventEntity->StatusEvent = 9 // Close door
 66: 0x021D [0x1C] WAIT(150* ticks)
 67: 0x0220 [0x46] CAMERA_CONTROL: Restore default settings
 68: 0x0222 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 69: 0x0233 [0x21] END_EVENT
 70: 0x0234 [0x00] END_REQSTACK()
```

### Event 12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0235   |
| Data Size    | 17 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0230:                20 01 42  4C 1C 0E 80 48 0F 80 23        .BL...H..#
0240: 4D 1C 0E 80 21 00                                 M...!.          
```

#### Opcodes

```
  0: 0x0235 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0237 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0238 [0x4C] EventEntity->StatusEvent = 8 // Open door
  3: 0x0239 [0x1C] WAIT(150* ticks)
  4: 0x023C [0x48] [System] [161*]:
    → "You see nothing of particular interest."
  5: 0x023F [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0240 [0x4D] EventEntity->StatusEvent = 9 // Close door
  7: 0x0241 [0x1C] WAIT(150* ticks)
  8: 0x0244 [0x21] END_EVENT
  9: 0x0245 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0246  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0240:                   4C 00                                 L.        
```

#### Opcodes

```
  0: 0x0246 [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x0247 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0248  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0240:                          4D 00                            M.      
```

#### Opcodes

```
  0: 0x0248 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0249 [0x00] END_REQSTACK()
```
