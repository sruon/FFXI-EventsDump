# 16880000 - Undulating Confluence

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Misareaux Coast (ID: 25) |
| Block Size       | 1100 bytes               |
| Total Events     | 8                        |
| References Count | 20                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [14](#event-14)          | 0x0001       |    946 |            103 |
| [15](#event-15)          | 0x03B3       |      1 |              1 |
| [16](#event-16)          | 0x03B4       |      1 |              1 |
| [17](#event-17)          | 0x03B5       |      1 |              1 |
| [18](#event-18)          | 0x03B6       |      1 |              1 |
| [65535.1](#event-655351) | 0x03B7       |     10 |              2 |
| [65535.2](#event-655352) | 0x03C1       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1B80      |        7040 |
|       1 | 0x0001      |           1 |
|       2 | 0x0000      |           0 |
|       3 | 0x40000000  |  1073741824 |
|       4 | 0x00C8      |         200 |
|       5 | 0x003C      |          60 |
|       6 | 0x0013      |          19 |
|       7 | 0xFFFF4A2D  |  4294920749 |
|       8 | 0x8B3CB     |      570315 |
|       9 | 0xFFFFA420  |  4294943776 |
|      10 | 0x090D      |        2317 |
|      11 | 0x02FE      |         766 |
|      12 | 0x00C9      |         201 |
|      13 | 0x007B      |         123 |
|      14 | 0x0078      |         120 |
|      15 | 0x001E      |          30 |
|      16 | 0x002D      |          45 |
|      17 | 0x0002      |           2 |
|      18 | 0x00D7      |         215 |
|      19 | 0x007F      |         127 |

## String References

- **7040**: Jump into the vortex? [Off we go!/Not just yet.]

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

### Event 14

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 946 bytes |
| Instructions | 47        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4A F0 FF FF 7F F8 FF  FF 7F 6F 76 F0 FF FF 7F   J........ov....
0010: 24 00 80 01 80 02 80 25  02 00 10 02 80 00 2D 00  $......%......-.
0020: 42 43 00 43 01 03 01 10  01 80 01 40 00 02 00 10  BC.C.......@....
0030: 01 80 00 40 00 03 01 10  03 80 01 20 01 01 40 00  ...@....... ..@.
0040: 42 46 01 45 04 80 F0 FF  FF 7F F0 FF FF 7F 66 64  BF.E..........fd
0050: 6F 31 02 80 1C 05 80 38  06 80 BA F0 FF FF 7F 07  o1.....8........
0060: 80 08 80 09 80 0A 80 80  F0 FF FF 7F 45 0B 80 F8  ............E...
0070: FF FF 7F F8 FF FF 7F 73  30 30 30 02 80 45 04 80  .......s000..E..
0080: F0 FF FF 7F F0 FF FF 7F  66 64 69 31 02 80 1C 05  ........fdi1....
0090: 80 45 04 80 F0 FF FF 7F  F0 FF FF 7F 62 6C 6F 6E  .E..........blon
00A0: 02 80 45 0C 80 F0 FF FF  7F F0 FF FF 7F 62 6C 6F  ..E..........blo
00B0: 6E 02 80 45 04 80 F0 FF  FF 7F F0 FF FF 7F 6F 76  n..E..........ov
00C0: 6C 31 02 80 D0 0D 80 F0  FF FF 7F F0 FF FF 7F 6D  l1.............m
00D0: 61 69 6E 02 80 1C 05 80  92 01 F0 FF FF 7F 1C 0E  ain.............
00E0: 80 45 0C 80 F0 FF FF 7F  F0 FF FF 7F 77 68 6F 31  .E..........who1
00F0: 02 80 55 0C 80 F0 FF FF  7F F0 FF FF 7F 77 68 6F  ..U..........who
0100: 31 1C 05 80 45 04 80 F0  FF FF 7F F0 FF FF 7F 62  1...E..........b
0110: 6C 6F 66 02 80 1C 0F 80  1A 85 01 1A A6 01 46 00  lof...........F.
0120: 21 00 45 04 80 F0 FF FF  7F F0 FF FF 7F 66 64 69  !.E..........fdi
0130: 30 02 80 55 04 80 F0 FF  FF 7F F0 FF FF 7F 66 64  0..U..........fd
0140: 69 30 1B 45 04 80 F0 FF  FF 7F F0 FF FF 7F 66 64  i0.E..........fd
0150: 6F 30 02 80 55 04 80 F0  FF FF 7F F0 FF FF 7F 66  o0..U..........f
0160: 64 6F 30 1B 45 04 80 F0  FF FF 7F F0 FF FF 7F 66  do0.E..........f
0170: 64 69 31 02 80 55 04 80  F0 FF FF 7F F0 FF FF 7F  di1..U..........
0180: 66 64 69 31 1B 45 04 80  F0 FF FF 7F F0 FF FF 7F  fdi1.E..........
0190: 66 64 6F 31 02 80 55 04  80 F0 FF FF 7F F0 FF FF  fdo1..U.........
01A0: 7F 66 64 6F 31 1B 45 0C  80 F0 FF FF 7F F0 FF FF  .fdo1.E.........
01B0: 7F 77 68 69 31 02 80 55  0C 80 F0 FF FF 7F F0 FF  .whi1..U........
01C0: FF 7F 77 68 69 31 1B 45  0C 80 F0 FF FF 7F F0 FF  ..whi1.E........
01D0: FF 7F 77 68 6F 31 02 80  55 0C 80 F0 FF FF 7F F0  ..who1..U.......
01E0: FF FF 7F 77 68 6F 31 1B  45 0C 80 F0 FF FF 7F F0  ...who1.E.......
01F0: FF FF 7F 77 68 6F 32 02  80 55 0C 80 F0 FF FF 7F  ...who2..U......
0200: F0 FF FF 7F 77 68 6F 32  1B 45 0C 80 F0 FF FF 7F  ....who2.E......
0210: F0 FF FF 7F 77 68 6F 33  02 80 55 0C 80 F0 FF FF  ....who3..U.....
0220: 7F F0 FF FF 7F 77 68 6F  33 1B 62 01 80 F0 FF FF  .....who3.b.....
0230: 7F F0 FF FF 7F 6D 61 69  6E 02 80 1C 10 80 45 04  .....main.....E.
0240: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 02 80 55  .........fdo1..U
0250: 04 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 1B 45  ..........fdo1.E
0260: 04 80 F0 FF FF 7F F0 FF  FF 7F 66 64 69 31 02 80  ..........fdi1..
0270: 62 11 80 F0 FF FF 7F F0  FF FF 7F 6D 61 69 6E 02  b..........main.
0280: 80 1C 0F 80 55 04 80 F0  FF FF 7F F0 FF FF 7F 66  ....U..........f
0290: 64 69 31 1B 45 04 80 F0  FF FF 7F F0 FF FF 7F 62  di1.E..........b
02A0: 6C 6F 6E 02 80 45 0C 80  F0 FF FF 7F F0 FF FF 7F  lon..E..........
02B0: 62 6C 6F 6E 02 80 1B 45  0C 80 F0 FF FF 7F F0 FF  blon...E........
02C0: FF 7F 77 68 69 30 02 80  55 0C 80 F0 FF FF 7F F0  ..whi0..U.......
02D0: FF FF 7F 77 68 69 30 1B  45 0C 80 F0 FF FF 7F F0  ...whi0.E.......
02E0: FF FF 7F 77 68 6F 30 02  80 55 0C 80 F0 FF FF 7F  ...who0..U......
02F0: F0 FF FF 7F 77 68 6F 30  1B 45 12 80 F0 FF FF 7F  ....who0.E......
0300: F0 FF FF 7F 65 66 6F 6E  02 80 55 12 80 F0 FF FF  ....efon..U.....
0310: 7F F0 FF FF 7F 65 66 6F  6E 1B 45 04 80 F0 FF FF  .....efon.E.....
0320: 7F F0 FF FF 7F 66 64 69  73 02 80 1B 45 04 80 F0  .....fdis...E...
0330: FF FF 7F F0 FF FF 7F 66  64 6F 73 02 80 55 04 80  .......fdos..U..
0340: F0 FF FF 7F F0 FF FF 7F  66 64 6F 73 1B 45 04 80  ........fdos.E..
0350: F0 FF FF 7F F0 FF FF 7F  66 64 69 66 02 80 1B 45  ........fdif...E
0360: 04 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 66 02 80  ..........fdof..
0370: 55 04 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 66 1B  U..........fdof.
0380: 45 04 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 70 02  E..........fdip.
0390: 80 1B 45 04 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..E..........fdo
03A0: 70 02 80 55 04 80 F0 FF  FF 7F F0 FF FF 7F 66 64  p..U..........fd
03B0: 6F 70 1B                                          op.             
```

#### Opcodes

```
  0: 0x0001 [0x4A] LocalPlayer looks at EventEntity
  1: 0x000A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x000B [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
  3: 0x0010 [0x24] CREATE_DIALOG(message_id=7040*, default_option=1*, option_flags=0*)
    → "Jump into the vortex? [Off we go!/Not just yet.]"
  4: 0x0017 [0x25] WAIT_DIALOG_SELECT()
  5: 0x0018 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x002D
  6: 0x0020 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  7: 0x0021 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  8: 0x0023 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  9: 0x0025 [0x03] Work_Zone[1] = 1*
 10: 0x002A [0x01] GOTO 0x0040
 11: 0x002D [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0040
 12: 0x0035 [0x03] Work_Zone[1] = 1073741824*
 13: 0x003A [0x01] GOTO 0x0120

SUBROUTINE_0040:
 14: 0x0040 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 15: 0x0041 [0x46] CAMERA_CONTROL: Disable user control
 16: 0x0043 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 17: 0x0054 [0x1C] WAIT(60* ticks)
 18: 0x0057 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 19: 0x005A [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-46.547*, pos_z=570.315*, pos_y=-23.520*, direction=203.6°*)
 20: 0x0067 [0x80] LOAD_WAIT(entity=LocalPlayer)
 21: 0x006C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s000" with entities [EventEntity, EventEntity], work=[766*, 0*]
 22: 0x007D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 23: 0x008E [0x1C] WAIT(60* ticks)
 24: 0x0091 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 25: 0x00A2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 26: 0x00B3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 27: 0x00C4 [0xD0] LOAD_SCHEDULED_TASK_ALT5: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[123*, 0*]
 28: 0x00D5 [0x1C] WAIT(60* ticks)
 29: 0x00D8 [0x92] LocalPlayer->Render.Flags3 ^= 0x01
 30: 0x00DE [0x1C] WAIT(120* ticks)
 31: 0x00E1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 32: 0x00F2 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=201*
 33: 0x0101 [0x1C] WAIT(60* ticks)
 34: 0x0104 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 35: 0x0115 [0x1C] WAIT(30* ticks)
 36: 0x0118 [0x1A] CALL_SUBROUTINE(address=0x0185)
 37: 0x011B [0x1A] CALL_SUBROUTINE(address=0x01A6)
 38: 0x011E [0x46] CAMERA_CONTROL: Restore default settings

SUBROUTINE_0120:
 39: 0x0120 [0x21] END_EVENT
 40: 0x0121 [0x00] END_REQSTACK()

SUBROUTINE_0185:
 41: 0x0185 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 42: 0x0196 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 43: 0x01A5 [0x1B] RETURN

SUBROUTINE_01A6:
 44: 0x01A6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 45: 0x01B7 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=201*
 46: 0x01C6 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x003D [0x01] GOTO 0x0040
# Dead code (unreachable instructions):
     0x0122 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0133 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0142 [0x1B] RETURN
     0x0143 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0154 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0163 [0x1B] RETURN
     0x0164 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0175 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0184 [0x1B] RETURN
# Dead code (unreachable instructions):
     0x01C7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x01D8 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=201*
     0x01E7 [0x1B] RETURN
     0x01E8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who2" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x01F9 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who2" with entities [LocalPlayer, LocalPlayer], work=201*
     0x0208 [0x1B] RETURN
     0x0209 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who3" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x021A [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who3" with entities [LocalPlayer, LocalPlayer], work=201*
     0x0229 [0x1B] RETURN
     0x022A [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
     0x023B [0x1C] WAIT(45* ticks)
     0x023E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x024F [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x025E [0x1B] RETURN
     0x025F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0270 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[2*, 0*]
     0x0281 [0x1C] WAIT(30* ticks)
     0x0284 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0293 [0x1B] RETURN
     0x0294 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x02A5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x02B6 [0x1B] RETURN
     0x02B7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi0" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x02C8 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "whi0" with entities [LocalPlayer, LocalPlayer], work=201*
     0x02D7 [0x1B] RETURN
     0x02D8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who0" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
     0x02E9 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who0" with entities [LocalPlayer, LocalPlayer], work=201*
     0x02F8 [0x1B] RETURN
     0x02F9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "efon" with entities [LocalPlayer, LocalPlayer], work=[215*, 0*]
     0x030A [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "efon" with entities [LocalPlayer, LocalPlayer], work=215*
     0x0319 [0x1B] RETURN
     0x031A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdis" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x032B [0x1B] RETURN
     0x032C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdos" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x033D [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdos" with entities [LocalPlayer, LocalPlayer], work=200*
     0x034C [0x1B] RETURN
     0x034D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdif" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x035E [0x1B] RETURN
     0x035F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0370 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdof" with entities [LocalPlayer, LocalPlayer], work=200*
     0x037F [0x1B] RETURN
     0x0380 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdip" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0391 [0x1B] RETURN
     0x0392 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdop" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x03A3 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdop" with entities [LocalPlayer, LocalPlayer], work=200*
     0x03B2 [0x1B] RETURN
```

### Event 15

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03B3  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03B0:          00                                          .            
```

#### Opcodes

```
  0: 0x03B3 [0x00] END_REQSTACK()
```

### Event 16

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03B4  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03B0:             00                                        .           
```

#### Opcodes

```
  0: 0x03B4 [0x00] END_REQSTACK()
```

### Event 17

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03B5  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03B0:                00                                      .          
```

#### Opcodes

```
  0: 0x03B5 [0x00] END_REQSTACK()
```

### Event 18

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03B6  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03B0:                   00                                    .         
```

#### Opcodes

```
  0: 0x03B6 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x03B7   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03B0:                      6C  F0 FF FF 7F 02 80 01 80         l........
03C0: 00                                                .               
```

#### Opcodes

```
  0: 0x03B7 [0x6C] FADE_ENTITY_COLOR(entity_id=LocalPlayer, end_alpha=0*, fade_time=1*)
  1: 0x03C0 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x03C1   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03C0:    6C F0 FF FF 7F 13 80  01 80 00                  l.........     
```

#### Opcodes

```
  0: 0x03C1 [0x6C] FADE_ENTITY_COLOR(entity_id=LocalPlayer, end_alpha=127*, fade_time=1*)
  1: 0x03CA [0x00] END_REQSTACK()
```
