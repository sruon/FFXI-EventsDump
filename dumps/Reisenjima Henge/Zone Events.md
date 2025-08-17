# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Reisenjima Henge (ID: 292) |
| Block Size       | 1268 bytes                 |
| Total Events     | 6                          |
| References Count | 52                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [65534](#event-65534) | 0x0001       |      1 |              1 |
| [10001](#event-10001) | 0x0002       |     26 |              7 |
| [10000](#event-10000) | 0x001C       |     66 |             12 |
| [1001](#event-1001)   | 0x005E       |    863 |            126 |
| [1002](#event-1002)   | 0x03BD       |     63 |             13 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0000      |           0 |
|       2 | 0x0078      |         120 |
|       3 | 0x00A8      |         168 |
|       4 | 0x00A0      |         160 |
|       5 | 0x00C8      |         200 |
|       6 | 0x0003      |           3 |
|       7 | 0x000E      |          14 |
|       8 | 0xFFEEF8A0  |  4293851296 |
|       9 | 0xFFF33690  |  4294129296 |
|      10 | 0xFFF96880  |  4294535296 |
|      11 | 0x0E00      |        3584 |
|      12 | 0x0002      |           2 |
|      13 | 0xFFFC6A08  |  4294732296 |
|      14 | 0xFFF15A00  |  4294007296 |
|      15 | 0xFFFA52E0  |  4294595296 |
|      16 | 0xFFF3CB00  |  4294167296 |
|      17 | 0xBE6E0     |      780000 |
|      18 | 0xFFFF88DC  |  4294936796 |
|      19 | 0x0004      |           4 |
|      20 | 0x975E0     |      620000 |
|      21 | 0xFFEFAC50  |  4293897296 |
|      22 | 0x0226      |         550 |
|      23 | 0x0C00      |        3072 |
|      24 | 0x0005      |           5 |
|      25 | 0x116520    |     1140000 |
|      26 | 0xFFFB4CE0  |  4294659296 |
|      27 | 0x0006      |           6 |
|      28 | 0xFFFCC3E0  |  4294755296 |
|      29 | 0x0400      |        1024 |
|      30 | 0x0007      |           7 |
|      31 | 0x119400    |     1152000 |
|      32 | 0x9E340     |      648000 |
|      33 | 0x000F      |          15 |
|      34 | 0x0A00      |        2560 |
|      35 | 0x0008      |           8 |
|      36 | 0xC15C0     |      792000 |
|      37 | 0x0600      |        1536 |
|      38 | 0x0009      |           9 |
|      39 | 0xFFF37CE0  |  4294147296 |
|      40 | 0x000A      |          10 |
|      41 | 0x000B      |          11 |
|      42 | 0x000C      |          12 |
|      43 | 0x000D      |          13 |
|      44 | 0x0010      |          16 |
|      45 | 0xF4240     |     1000000 |
|      46 | 0xAFC80     |      720000 |
|      47 | 0x0011      |          17 |
|      48 | 0x003C      |          60 |
|      49 | 0x00A9      |         169 |
|      50 | 0x1CA3      |        7331 |
|      51 | 0x00C9      |         201 |

## String References

- **7331**: The light contains...something other than peace and serenity!

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

### Event 65534

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 10001

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 26 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       20 01 42 62 00 80  F0 FF FF 7F F0 FF FF 7F     .Bb..........
0010: 6D 61 69 6E 01 80 1C 02  80 30 21 00              main.....0!.    
```

#### Opcodes

```
  0: 0x0002 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0004 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0005 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
  3: 0x0016 [0x1C] WAIT(120* ticks)
  4: 0x0019 [0x30] SET_UCOFF_CONTINUE_ZERO()
  5: 0x001A [0x21] END_EVENT
  6: 0x001B [0x00] END_REQSTACK()
```

### Event 10000

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001C   |
| Data Size    | 66 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                      20 01 42 3E               .B>
0020: 09 10 00 80 2C 00 4E 01  F0 FF FF 7F 3E 09 10 01  ....,.N.....>...
0030: 80 47 00 D0 03 80 F0 FF  FF 7F F0 FF FF 7F 6D 61  .G............ma
0040: 69 6E 01 80 1C 04 80 45  05 80 F0 FF FF 7F F0 FF  in.....E........
0050: FF 7F 66 64 6F 31 01 80  1C 02 80 30 21 00        ..fdo1.....0!.  
```

#### Opcodes

```
  0: 0x001C [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x001E [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x001F [0x3E] IF !(Work_Zone[9] bit 1*) GOTO 0x002C
  3: 0x0026 [0x4E] SET_ENTITY_HIDE_FLAG: Hide LocalPlayer
  4: 0x002C [0x3E] IF !(Work_Zone[9] bit 0*) GOTO 0x0047
  5: 0x0033 [0xD0] LOAD_SCHEDULED_TASK_ALT5: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[168*, 0*]
  6: 0x0044 [0x1C] WAIT(160* ticks)
  7: 0x0047 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x0058 [0x1C] WAIT(120* ticks)
  9: 0x005B [0x30] SET_UCOFF_CONTINUE_ZERO()
 10: 0x005C [0x21] END_EVENT
 11: 0x005D [0x00] END_REQSTACK()
```

### Event 1001

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x005E    |
| Data Size    | 863 bytes |
| Instructions | 126       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            03 00                ..
0060: 00 02 10 20 01 42 02 00  00 06 80 80 74 00 1A 5C  ... .B......t..\
0070: 03 01 85 00 02 00 00 07  80 80 82 00 1A 5C 03 01  .............\..
0080: 85 00 1A FE 02 03 01 10  00 80 02 00 00 01 80 80  ................
0090: 9A 00 03 01 10 01 80 01  DA 02 02 00 00 00 80 80  ................
00A0: BE 00 BA F0 FF FF 7F 08  80 09 80 0A 80 0B 80 47  ...............G
00B0: 00 08 80 09 80 0A 80 0B  80 47 01 01 DA 02 02 00  .........G......
00C0: 00 0C 80 80 E2 00 BA F0  FF FF 7F 0D 80 0E 80 0F  ................
00D0: 80 0B 80 47 00 0D 80 0E  80 0F 80 0B 80 47 01 01  ...G.........G..
00E0: DA 02 02 00 00 06 80 80  06 01 BA F0 FF FF 7F 10  ................
00F0: 80 11 80 12 80 01 80 47  00 10 80 11 80 12 80 01  .......G........
0100: 80 47 01 01 DA 02 02 00  00 13 80 80 2A 01 BA F0  .G..........*...
0110: FF FF 7F 14 80 15 80 16  80 17 80 47 00 14 80 15  ...........G....
0120: 80 16 80 17 80 47 01 01  DA 02 02 00 00 18 80 80  .....G..........
0130: 4E 01 BA F0 FF FF 7F 19  80 1A 80 16 80 17 80 47  N..............G
0140: 00 19 80 1A 80 16 80 17  80 47 01 01 DA 02 02 00  .........G......
0150: 00 1B 80 80 72 01 BA F0  FF FF 7F 19 80 1C 80 16  ....r...........
0160: 80 1D 80 47 00 19 80 1C  80 16 80 1D 80 47 01 01  ...G.........G..
0170: DA 02 02 00 00 1E 80 80  96 01 BA F0 FF FF 7F 1F  ................
0180: 80 20 80 21 80 22 80 47  00 1F 80 20 80 21 80 22  . .!.".G... .!."
0190: 80 47 01 01 DA 02 02 00  00 23 80 80 BA 01 BA F0  .G.......#......
01A0: FF FF 7F 1F 80 24 80 21  80 25 80 47 00 1F 80 24  .....$.!.%.G...$
01B0: 80 21 80 25 80 47 01 01  DA 02 02 00 00 26 80 80  .!.%.G.......&..
01C0: DE 01 BA F0 FF FF 7F 27  80 11 80 12 80 01 80 47  .......'.......G
01D0: 00 27 80 11 80 12 80 01  80 47 01 01 DA 02 02 00  .'.......G......
01E0: 00 28 80 80 02 02 BA F0  FF FF 7F 27 80 11 80 12  .(.........'....
01F0: 80 01 80 47 00 27 80 11  80 12 80 01 80 47 01 01  ...G.'.......G..
0200: DA 02 02 00 00 29 80 80  26 02 BA F0 FF FF 7F 27  .....)..&......'
0210: 80 11 80 12 80 01 80 47  00 27 80 11 80 12 80 01  .......G.'......
0220: 80 47 01 01 DA 02 02 00  00 2A 80 80 4A 02 BA F0  .G.......*..J...
0230: FF FF 7F 27 80 11 80 12  80 01 80 47 00 27 80 11  ...'.......G.'..
0240: 80 12 80 01 80 47 01 01  DA 02 02 00 00 2B 80 80  .....G.......+..
0250: 6E 02 BA F0 FF FF 7F 27  80 11 80 12 80 01 80 47  n......'.......G
0260: 00 27 80 11 80 12 80 01  80 47 01 01 DA 02 02 00  .'.......G......
0270: 00 07 80 80 92 02 BA F0  FF FF 7F 10 80 11 80 12  ................
0280: 80 01 80 47 00 10 80 11  80 12 80 01 80 47 01 01  ...G.........G..
0290: DA 02 02 00 00 2C 80 80  B6 02 BA F0 FF FF 7F 2D  .....,.........-
02A0: 80 2E 80 01 80 01 80 47  00 2D 80 2E 80 01 80 01  .......G.-......
02B0: 80 47 01 01 DA 02 02 00  00 2F 80 80 DA 02 BA F0  .G......./......
02C0: FF FF 7F 27 80 11 80 12  80 01 80 47 00 27 80 11  ...'.......G.'..
02D0: 80 12 80 01 80 47 01 01  DA 02 02 00 00 06 80 80  .....G..........
02E0: E8 02 1A 88 03 01 F9 02  02 00 00 07 80 80 F6 02  ................
02F0: 1A 88 03 01 F9 02 1A 27  03 2E 20 00 21 00 D0 03  .......'.. .!...
0300: 80 F0 FF FF 7F F0 FF FF  7F 6D 61 69 6E 01 80 1C  .........main...
0310: 04 80 45 05 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..E..........fdo
0320: 31 01 80 1C 30 80 1B 45  05 80 F0 FF FF 7F F0 FF  1...0..E........
0330: FF 7F 66 64 69 31 01 80  D0 31 80 F0 FF FF 7F F0  ..fdi1...1......
0340: FF FF 7F 6D 61 69 6E 01  80 1C 04 80 55 05 80 F0  ...main.....U...
0350: FF FF 7F F0 FF FF 7F 66  64 69 31 1B D0 03 80 F0  .......fdi1.....
0360: FF FF 7F F0 FF FF 7F 6D  61 69 6E 01 80 1C 04 80  .......main.....
0370: 48 32 80 45 33 80 F0 FF  FF 7F F0 FF FF 7F 77 68  H2.E3.........wh
0380: 6F 31 01 80 1C 30 80 1B  45 33 80 F0 FF FF 7F F0  o1...0..E3......
0390: FF FF 7F 77 68 69 31 01  80 D0 31 80 F0 FF FF 7F  ...whi1...1.....
03A0: F0 FF FF 7F 6D 61 69 6E  01 80 1C 04 80 55 33 80  ....main.....U3.
03B0: F0 FF FF 7F F0 FF FF 7F  77 68 69 31 1B           ........whi1.   
```

#### Opcodes

```
  0: 0x005E [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  1: 0x0063 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x0065 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  3: 0x0066 [0x02] IF !(ExtData[1]->WorkLocal[0] == 3*) GOTO 0x0074
  4: 0x006E [0x1A] CALL_SUBROUTINE(address=0x035C)
  5: 0x0071 [0x01] GOTO 0x0085
  6: 0x0074 [0x02] IF !(ExtData[1]->WorkLocal[0] == 14*) GOTO 0x0082
  7: 0x007C [0x1A] CALL_SUBROUTINE(address=0x035C)
  8: 0x007F [0x01] GOTO 0x0085
  9: 0x0082 [0x1A] CALL_SUBROUTINE(address=0x02FE)

SUBROUTINE_0085:
 10: 0x0085 [0x03] Work_Zone[1] = 1*
 11: 0x008A [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x009A
 12: 0x0092 [0x03] Work_Zone[1] = 0*
 13: 0x0097 [0x01] GOTO 0x02DA
 14: 0x009A [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x00BE
 15: 0x00A2 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-1116.000*, pos_z=-838.000*, pos_y=-432.000*, direction=315.0°*)
 16: 0x00AF [0x47] UPDATE_PLAYER_POS(-1116.000*, -838.000*, -432.000*, yaw=315.0°*)
 17: 0x00B9 [0x47] WAIT_PLAYER_POS_UPDATE
 18: 0x00BB [0x01] GOTO 0x02DA
 19: 0x00BE [0x02] IF !(ExtData[1]->WorkLocal[0] == 2*) GOTO 0x00E2
 20: 0x00C6 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-235.000*, pos_z=-960.000*, pos_y=-372.000*, direction=315.0°*)
 21: 0x00D3 [0x47] UPDATE_PLAYER_POS(-235.000*, -960.000*, -372.000*, yaw=315.0°*)
 22: 0x00DD [0x47] WAIT_PLAYER_POS_UPDATE
 23: 0x00DF [0x01] GOTO 0x02DA
 24: 0x00E2 [0x02] IF !(ExtData[1]->WorkLocal[0] == 3*) GOTO 0x0106
 25: 0x00EA [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-800.000*, pos_z=780.000*, pos_y=-30.500*, direction=0.0°*)
 26: 0x00F7 [0x47] UPDATE_PLAYER_POS(-800.000*, 780.000*, -30.500*, yaw=0.0°*)
 27: 0x0101 [0x47] WAIT_PLAYER_POS_UPDATE
 28: 0x0103 [0x01] GOTO 0x02DA
 29: 0x0106 [0x02] IF !(ExtData[1]->WorkLocal[0] == 4*) GOTO 0x012A
 30: 0x010E [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=620.000*, pos_z=-1070.000*, pos_y=0.550*, direction=270.0°*)
 31: 0x011B [0x47] UPDATE_PLAYER_POS(620.000*, -1070.000*, 0.550*, yaw=270.0°*)
 32: 0x0125 [0x47] WAIT_PLAYER_POS_UPDATE
 33: 0x0127 [0x01] GOTO 0x02DA
 34: 0x012A [0x02] IF !(ExtData[1]->WorkLocal[0] == 5*) GOTO 0x014E
 35: 0x0132 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=1140.000*, pos_z=-308.000*, pos_y=0.550*, direction=270.0°*)
 36: 0x013F [0x47] UPDATE_PLAYER_POS(1140.000*, -308.000*, 0.550*, yaw=270.0°*)
 37: 0x0149 [0x47] WAIT_PLAYER_POS_UPDATE
 38: 0x014B [0x01] GOTO 0x02DA
 39: 0x014E [0x02] IF !(ExtData[1]->WorkLocal[0] == 6*) GOTO 0x0172
 40: 0x0156 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=1140.000*, pos_z=-212.000*, pos_y=0.550*, direction=90.0°*)
 41: 0x0163 [0x47] UPDATE_PLAYER_POS(1140.000*, -212.000*, 0.550*, yaw=90.0°*)
 42: 0x016D [0x47] WAIT_PLAYER_POS_UPDATE
 43: 0x016F [0x01] GOTO 0x02DA
 44: 0x0172 [0x02] IF !(ExtData[1]->WorkLocal[0] == 7*) GOTO 0x0196
 45: 0x017A [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=1152.000*, pos_z=648.000*, pos_y=0.015*, direction=225.0°*)
 46: 0x0187 [0x47] UPDATE_PLAYER_POS(1152.000*, 648.000*, 0.015*, yaw=225.0°*)
 47: 0x0191 [0x47] WAIT_PLAYER_POS_UPDATE
 48: 0x0193 [0x01] GOTO 0x02DA
 49: 0x0196 [0x02] IF !(ExtData[1]->WorkLocal[0] == 8*) GOTO 0x01BA
 50: 0x019E [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=1152.000*, pos_z=792.000*, pos_y=0.015*, direction=135.0°*)
 51: 0x01AB [0x47] UPDATE_PLAYER_POS(1152.000*, 792.000*, 0.015*, yaw=135.0°*)
 52: 0x01B5 [0x47] WAIT_PLAYER_POS_UPDATE
 53: 0x01B7 [0x01] GOTO 0x02DA
 54: 0x01BA [0x02] IF !(ExtData[1]->WorkLocal[0] == 9*) GOTO 0x01DE
 55: 0x01C2 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-820.000*, pos_z=780.000*, pos_y=-30.500*, direction=0.0°*)
 56: 0x01CF [0x47] UPDATE_PLAYER_POS(-820.000*, 780.000*, -30.500*, yaw=0.0°*)
 57: 0x01D9 [0x47] WAIT_PLAYER_POS_UPDATE
 58: 0x01DB [0x01] GOTO 0x02DA
 59: 0x01DE [0x02] IF !(ExtData[1]->WorkLocal[0] == 10*) GOTO 0x0202
 60: 0x01E6 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-820.000*, pos_z=780.000*, pos_y=-30.500*, direction=0.0°*)
 61: 0x01F3 [0x47] UPDATE_PLAYER_POS(-820.000*, 780.000*, -30.500*, yaw=0.0°*)
 62: 0x01FD [0x47] WAIT_PLAYER_POS_UPDATE
 63: 0x01FF [0x01] GOTO 0x02DA
 64: 0x0202 [0x02] IF !(ExtData[1]->WorkLocal[0] == 11*) GOTO 0x0226
 65: 0x020A [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-820.000*, pos_z=780.000*, pos_y=-30.500*, direction=0.0°*)
 66: 0x0217 [0x47] UPDATE_PLAYER_POS(-820.000*, 780.000*, -30.500*, yaw=0.0°*)
 67: 0x0221 [0x47] WAIT_PLAYER_POS_UPDATE
 68: 0x0223 [0x01] GOTO 0x02DA
 69: 0x0226 [0x02] IF !(ExtData[1]->WorkLocal[0] == 12*) GOTO 0x024A
 70: 0x022E [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-820.000*, pos_z=780.000*, pos_y=-30.500*, direction=0.0°*)
 71: 0x023B [0x47] UPDATE_PLAYER_POS(-820.000*, 780.000*, -30.500*, yaw=0.0°*)
 72: 0x0245 [0x47] WAIT_PLAYER_POS_UPDATE
 73: 0x0247 [0x01] GOTO 0x02DA
 74: 0x024A [0x02] IF !(ExtData[1]->WorkLocal[0] == 13*) GOTO 0x026E
 75: 0x0252 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-820.000*, pos_z=780.000*, pos_y=-30.500*, direction=0.0°*)
 76: 0x025F [0x47] UPDATE_PLAYER_POS(-820.000*, 780.000*, -30.500*, yaw=0.0°*)
 77: 0x0269 [0x47] WAIT_PLAYER_POS_UPDATE
 78: 0x026B [0x01] GOTO 0x02DA
 79: 0x026E [0x02] IF !(ExtData[1]->WorkLocal[0] == 14*) GOTO 0x0292
 80: 0x0276 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-800.000*, pos_z=780.000*, pos_y=-30.500*, direction=0.0°*)
 81: 0x0283 [0x47] UPDATE_PLAYER_POS(-800.000*, 780.000*, -30.500*, yaw=0.0°*)
 82: 0x028D [0x47] WAIT_PLAYER_POS_UPDATE
 83: 0x028F [0x01] GOTO 0x02DA
 84: 0x0292 [0x02] IF !(ExtData[1]->WorkLocal[0] == 16*) GOTO 0x02B6
 85: 0x029A [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=1000.000*, pos_z=720.000*, pos_y=0.000*, direction=0.0°*)
 86: 0x02A7 [0x47] UPDATE_PLAYER_POS(1000.000*, 720.000*, 0.000*, yaw=0.0°*)
 87: 0x02B1 [0x47] WAIT_PLAYER_POS_UPDATE
 88: 0x02B3 [0x01] GOTO 0x02DA
 89: 0x02B6 [0x02] IF !(ExtData[1]->WorkLocal[0] == 17*) GOTO 0x02DA
 90: 0x02BE [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-820.000*, pos_z=780.000*, pos_y=-30.500*, direction=0.0°*)
 91: 0x02CB [0x47] UPDATE_PLAYER_POS(-820.000*, 780.000*, -30.500*, yaw=0.0°*)
 92: 0x02D5 [0x47] WAIT_PLAYER_POS_UPDATE
 93: 0x02D7 [0x01] GOTO 0x02DA

SUBROUTINE_02DA:
 94: 0x02DA [0x02] IF !(ExtData[1]->WorkLocal[0] == 3*) GOTO 0x02E8
 95: 0x02E2 [0x1A] CALL_SUBROUTINE(address=0x0388)
 96: 0x02E5 [0x01] GOTO 0x02F9
 97: 0x02E8 [0x02] IF !(ExtData[1]->WorkLocal[0] == 14*) GOTO 0x02F6
 98: 0x02F0 [0x1A] CALL_SUBROUTINE(address=0x0388)
 99: 0x02F3 [0x01] GOTO 0x02F9
100: 0x02F6 [0x1A] CALL_SUBROUTINE(address=0x0327)

SUBROUTINE_02F9:
101: 0x02F9 [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
102: 0x02FA [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
103: 0x02FC [0x21] END_EVENT
104: 0x02FD [0x00] END_REQSTACK()

SUBROUTINE_02FE:
105: 0x02FE [0xD0] LOAD_SCHEDULED_TASK_ALT5: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[168*, 0*]
106: 0x030F [0x1C] WAIT(160* ticks)
107: 0x0312 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
108: 0x0323 [0x1C] WAIT(60* ticks)
109: 0x0326 [0x1B] RETURN

SUBROUTINE_0327:
110: 0x0327 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
111: 0x0338 [0xD0] LOAD_SCHEDULED_TASK_ALT5: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[169*, 0*]
112: 0x0349 [0x1C] WAIT(160* ticks)
113: 0x034C [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
114: 0x035B [0x1B] RETURN

SUBROUTINE_035C:
115: 0x035C [0xD0] LOAD_SCHEDULED_TASK_ALT5: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[168*, 0*]
116: 0x036D [0x1C] WAIT(160* ticks)
117: 0x0370 [0x48] [System] [7331*]:
    → "The light contains...something other than peace and serenity!"
118: 0x0373 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
119: 0x0384 [0x1C] WAIT(60* ticks)
120: 0x0387 [0x1B] RETURN

SUBROUTINE_0388:
121: 0x0388 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
122: 0x0399 [0xD0] LOAD_SCHEDULED_TASK_ALT5: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[169*, 0*]
123: 0x03AA [0x1C] WAIT(160* ticks)
124: 0x03AD [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=201*
125: 0x03BC [0x1B] RETURN
```

### Event 1002

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x03BD   |
| Data Size    | 63 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03B0:                                         20 01 42                .B
03C0: 45 33 80 F0 FF FF 7F F0  FF FF 7F 77 68 6F 31 01  E3.........who1.
03D0: 80 1C 30 80 47 00 27 80  11 80 12 80 01 80 47 01  ..0.G.'.......G.
03E0: 1C 30 80 45 33 80 F0 FF  FF 7F F0 FF FF 7F 77 68  .0.E3.........wh
03F0: 69 31 01 80 1C 30 80 2E  20 00 21 00              i1...0.. .!.    
```

#### Opcodes

```
  0: 0x03BD [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x03BF [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x03C0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  3: 0x03D1 [0x1C] WAIT(60* ticks)
  4: 0x03D4 [0x47] UPDATE_PLAYER_POS(-820.000*, 780.000*, -30.500*, yaw=0.0°*)
  5: 0x03DE [0x47] WAIT_PLAYER_POS_UPDATE
  6: 0x03E0 [0x1C] WAIT(60* ticks)
  7: 0x03E3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  8: 0x03F4 [0x1C] WAIT(60* ticks)
  9: 0x03F7 [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 10: 0x03F8 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 11: 0x03FA [0x21] END_EVENT
 12: 0x03FB [0x00] END_REQSTACK()
```
