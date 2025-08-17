# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Dangruf Wadi (ID: 191) |
| Block Size       | 1848 bytes             |
| Total Events     | 14                     |
| References Count | 63                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65534](#event-65534)    | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     37 |              5 |
| [65535.2](#event-655352) | 0x0027       |    185 |             37 |
| [100](#event-100)        | 0x00E0       |    122 |             25 |
| [103](#event-103)        | 0x015A       |     13 |              3 |
| [104](#event-104)        | 0x0167       |     13 |              3 |
| [10](#event-10)          | 0x0174       |    329 |             67 |
| [11](#event-11)          | 0x02BD       |    282 |             57 |
| [12](#event-12)          | 0x03D7       |    282 |             57 |
| [120](#event-120)        | 0x04F1       |     13 |              3 |
| [121](#event-121)        | 0x04FE       |     13 |              3 |
| [122](#event-122)        | 0x050B       |     13 |              3 |
| [150](#event-150)        | 0x0518       |    220 |             30 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0005      |           5 |
|       1 | 0x0001      |           1 |
|       2 | 0x0002      |           2 |
|       3 | 0x000A      |          10 |
|       4 | 0x0009      |           9 |
|       5 | 0x0046      |          70 |
|       6 | 0x008C      |         140 |
|       7 | 0x00D2      |         210 |
|       8 | 0x1CFE      |        7422 |
|       9 | 0x0000      |           0 |
|      10 | 0x0003      |           3 |
|      11 | 0x0004      |           4 |
|      12 | 0x0006      |           6 |
|      13 | 0xFFFE1D49  |  4294843721 |
|      14 | 0x20BB8     |      134072 |
|      15 | 0x0F83      |        3971 |
|      16 | 0x062E      |        1582 |
|      17 | 0xFFFFB973  |  4294949235 |
|      18 | 0x0772      |        1906 |
|      19 | 0xFFFFFF7F  |  4294967167 |
|      20 | 0x040A      |        1034 |
|      21 | 0xFFFDF7BB  |  4294834107 |
|      22 | 0x2081E     |      133150 |
|      23 | 0x01F4      |         500 |
|      24 | 0x0078      |         120 |
|      25 | 0x003C      |          60 |
|      26 | 0x0100      |         256 |
|      27 | 0x0400      |        1024 |
|      28 | 0x0168      |         360 |
|      29 | 0x0800      |        2048 |
|      30 | 0x01E0      |         480 |
|      31 | 0x0064      |         100 |
|      32 | 0x0E00      |        3584 |
|      33 | 0x0320      |         800 |
|      34 | 0xFFFFFFFF  |  4294967295 |
|      35 | 0x0A52      |        2642 |
|      36 | 0x0020      |          32 |
|      37 | 0xFFFCBF51  |  4294754129 |
|      38 | 0x16C36     |       93238 |
|      39 | 0x0080      |         128 |
|      40 | 0x0040      |          64 |
|      41 | 0x00F0      |         240 |
|      42 | 0x1000      |        4096 |
|      43 | 0x0010      |          16 |
|      44 | 0xFFFEFAD6  |  4294900438 |
|      45 | 0x8233D     |      533309 |
|      46 | 0x0E74      |        3700 |
|      47 | 0xFFFA5665  |  4294596197 |
|      48 | 0x37C62     |      228450 |
|      49 | 0x0F74      |        3956 |
|      50 | 0xFFFA4104  |  4294590724 |
|      51 | 0x6BF57     |      442199 |
|      52 | 0xFFFFFFF7  |  4294967287 |
|      53 | 0xFFF8F877  |  4294506615 |
|      54 | 0xFFFDDFE5  |  4294828005 |
|      55 | 0x0F8D      |        3981 |
|      56 | 0x0023      |          35 |
|      57 | 0x00C8      |         200 |
|      58 | 0x0EA6      |        3750 |
|      59 | 0x01F2      |         498 |
|      60 | 0x1D27      |        7463 |
|      61 | 0x1D28      |        7464 |
|      62 | 0x0687      |        1671 |

## String References

- **7422**: Where do you want to go? (This page scrolls down.) [Nowhere./San d'Oria./Windurst./Elevator in Ghelsba/Bastok/Ronfaure Forest]

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       03 00 00 07 7F 1A  4C 00 66 01 00 F8 FF FF    ......L.f.....
0010: 7F F8 FF FF 7F 73 68 61  30 53 F8 FF FF 7F F8 FF  .....sha0S......
0020: FF 7F 73 68 61 30 00                              ..sha0.         
```

#### Opcodes

```
  0: 0x0002 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x0007 [0x1A] CALL_SUBROUTINE(address=0x004C)
  2: 0x000A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x0019 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha0" with entities [EventEntity, EventEntity]
  4: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0027    |
| Data Size    | 185 bytes |
| Instructions | 13        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      03  00 00 07 7F 1A 4C 00 66         ......L.f
0030: 01 00 F8 FF FF 7F F8 FF  FF 7F 73 68 61 31 53 F8  ..........sha1S.
0040: FF FF 7F F8 FF FF 7F 73  68 61 31 00 03 01 00 00  .......sha1.....
0050: 00 02 01 00 00 80 05 61  00 08 01 00 01 80 01 66  .......a.......f
0060: 00 08 01 00 02 80 14 01  00 03 80 07 01 00 04 80  ................
0070: 1B 03 01 00 00 00 02 01  00 00 80 05 86 00 08 01  ................
0080: 00 01 80 01 8B 00 08 01  00 02 80 14 01 00 03 80  ................
0090: 07 01 00 05 80 1B 03 01  00 00 00 02 01 00 00 80  ................
00A0: 05 AB 00 08 01 00 01 80  01 B0 00 08 01 00 02 80  ................
00B0: 14 01 00 03 80 07 01 00  06 80 1B 03 01 00 00 00  ................
00C0: 02 01 00 00 80 05 D0 00  08 01 00 01 80 01 D5 00  ................
00D0: 08 01 00 02 80 14 01 00  03 80 07 01 00 07 80 1B  ................
```

#### Opcodes

```
  0: 0x0027 [0x03] ExtData[1]->WorkLocal[0] = Entity->Race
  1: 0x002C [0x1A] CALL_SUBROUTINE(address=0x004C)
  2: 0x002F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[1]
  3: 0x003E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [EventEntity, EventEntity]
  4: 0x004B [0x00] END_REQSTACK()

SUBROUTINE_004C:
  5: 0x004C [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
  6: 0x0051 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0061
  7: 0x0059 [0x08] ExtData[1]->WorkLocal[1] -= 1*
  8: 0x005E [0x01] GOTO 0x0066
  9: 0x0061 [0x08] ExtData[1]->WorkLocal[1] -= 2*

SUBROUTINE_0066:
 10: 0x0066 [0x14] ExtData[1]->WorkLocal[1] *= 10*
 11: 0x006B [0x07] ExtData[1]->WorkLocal[1] += 9*
 12: 0x0070 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0071 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x0076 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0086
     0x007E [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x0083 [0x01] GOTO 0x008B
     0x0086 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x008B [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x0090 [0x07] ExtData[1]->WorkLocal[1] += 70*
     0x0095 [0x1B] RETURN
     0x0096 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x009B [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x00AB
     0x00A3 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x00A8 [0x01] GOTO 0x00B0
     0x00AB [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x00B0 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x00B5 [0x07] ExtData[1]->WorkLocal[1] += 140*
     0x00BA [0x1B] RETURN
     0x00BB [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x00C0 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x00D0
     0x00C8 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x00CD [0x01] GOTO 0x00D5
     0x00D0 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x00D5 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x00DA [0x07] ExtData[1]->WorkLocal[1] += 210*
     0x00DF [0x1B] RETURN
```

### Event 100

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00E0    |
| Data Size    | 122 bytes |
| Instructions | 25        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0: 24 08 80 09 80 09 80 25  02 00 10 09 80 00 F8 00  $......%........
00F0: 03 01 10 09 80 01 58 01  02 00 10 01 80 00 08 01  ......X.........
0100: 03 01 10 01 80 01 58 01  02 00 10 02 80 00 18 01  ......X.........
0110: 03 01 10 02 80 01 58 01  02 00 10 0A 80 00 28 01  ......X.......(.
0120: 03 01 10 0A 80 01 58 01  02 00 10 0B 80 00 38 01  ......X.......8.
0130: 03 01 10 0B 80 01 58 01  02 00 10 00 80 00 48 01  ......X.......H.
0140: 03 01 10 00 80 01 58 01  02 00 10 0C 80 00 58 01  ......X.......X.
0150: 03 01 10 0C 80 01 58 01  21 00                    ......X.!.      
```

#### Opcodes

```
  0: 0x00E0 [0x24] CREATE_DIALOG(message_id=7422*, default_option=0*, option_flags=0*)
    → "Where do you want to go? (This page scrolls down.) [Nowhere./San d'Oria./Windurst./Elevator in Ghelsba/Bastok/Ronfaure Forest]"
  1: 0x00E7 [0x25] WAIT_DIALOG_SELECT()
  2: 0x00E8 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00F8
  3: 0x00F0 [0x03] Work_Zone[1] = 0*
  4: 0x00F5 [0x01] GOTO 0x0158
  5: 0x00F8 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0108
  6: 0x0100 [0x03] Work_Zone[1] = 1*
  7: 0x0105 [0x01] GOTO 0x0158
  8: 0x0108 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0118
  9: 0x0110 [0x03] Work_Zone[1] = 2*
 10: 0x0115 [0x01] GOTO 0x0158
 11: 0x0118 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0128
 12: 0x0120 [0x03] Work_Zone[1] = 3*
 13: 0x0125 [0x01] GOTO 0x0158
 14: 0x0128 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0138
 15: 0x0130 [0x03] Work_Zone[1] = 4*
 16: 0x0135 [0x01] GOTO 0x0158
 17: 0x0138 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x0148
 18: 0x0140 [0x03] Work_Zone[1] = 5*
 19: 0x0145 [0x01] GOTO 0x0158
 20: 0x0148 [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x0158
 21: 0x0150 [0x03] Work_Zone[1] = 6*
 22: 0x0155 [0x01] GOTO 0x0158

SUBROUTINE_0158:
 23: 0x0158 [0x21] END_EVENT
 24: 0x0159 [0x00] END_REQSTACK()
```

### Event 103

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x015A   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                47 00 0D 80 0E 80            G.....
0160: 0F 80 10 80 47 01 00                              ....G..         
```

#### Opcodes

```
  0: 0x015A [0x47] UPDATE_PLAYER_POS(-123.575*, 134.072*, 3.971*, yaw=139.0°*)
  1: 0x0164 [0x47] WAIT_PLAYER_POS_UPDATE
  2: 0x0166 [0x00] END_REQSTACK()
```

### Event 104

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0167   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                      47  00 11 80 12 80 13 80 14         G........
0170: 80 47 01 00                                       .G..            
```

#### Opcodes

```
  0: 0x0167 [0x47] UPDATE_PLAYER_POS(-18.061*, 1.906*, -0.129*, yaw=90.9°*)
  1: 0x0171 [0x47] WAIT_PLAYER_POS_UPDATE
  2: 0x0173 [0x00] END_REQSTACK()
```

### Event 10

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0174    |
| Data Size    | 329 bytes |
| Instructions | 67        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:             20 01 42 06  11 00 06 0A 00 06 0B 00       .B.........
0180: 06 0C 00 06 0D 00 3B F0  FF FF 7F 06 00 08 00 07  ......;.........
0190: 00 3A F0 FF FF 7F 09 00  64 05 00 06 00 08 00 15  .:......d.......
01A0: 80 16 80 02 05 00 17 80  02 AD 01 21 00 03 0E 00  ...........!....
01B0: 06 00 03 10 00 08 00 33  01 03 04 00 09 80 06 03  .......3........
01C0: 00 06 02 00 06 05 00 02  05 00 09 80 00 93 02 02  ................
01D0: 11 00 09 80 80 FB 01 17  0C 00 04 00 18 80 08 0C  ................
01E0: 00 18 80 08 0C 00 19 80  07 04 00 1A 80 02 04 00  ................
01F0: 1B 80 02 F8 01 0B 11 00  01 49 02 02 11 00 01 80  .........I......
0200: 80 22 02 17 0C 00 04 00  1C 80 08 0C 00 1C 80 07  ."..............
0210: 04 00 1A 80 02 04 00 1D  80 04 1F 02 0B 11 00 01  ................
0220: 49 02 02 11 00 02 80 80  44 02 17 0C 00 04 00 1E  I.......D.......
0230: 80 07 04 00 1F 80 02 04  00 20 80 04 41 02 0B 11  ......... ..A...
0240: 00 01 49 02 05 05 00 33  00 17 03 00 02 00 21 80  ..I....3......!.
0250: 08 03 00 21 80 14 03 00  22 80 17 0A 00 23 80 03  ...!...."....#..
0260: 00 16 0B 00 23 80 03 00  02 02 00 1B 80 05 75 02  ....#.........u.
0270: 07 02 00 24 80 07 06 00  0A 00 07 08 00 0B 00 07  ...$............
0280: 07 00 0C 00 37 06 00 08  00 07 00 09 00 1C 01 80  ....7...........
0290: 01 C7 01 14 0A 00 0A 80  14 0B 00 0A 80 14 0C 00  ................
02A0: 0A 80 07 06 00 0A 00 07  08 00 0B 00 07 07 00 0C  ................
02B0: 00 1F 00 06 00 08 00 07  00 1F 01 21 00           ...........!.   
```

#### Opcodes

```
  0: 0x0174 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0176 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0177 [0x06] ExtData[1]->WorkLocal[17] = 0
  3: 0x017A [0x06] ExtData[1]->WorkLocal[10] = 0
  4: 0x017D [0x06] ExtData[1]->WorkLocal[11] = 0
  5: 0x0180 [0x06] ExtData[1]->WorkLocal[12] = 0
  6: 0x0183 [0x06] ExtData[1]->WorkLocal[13] = 0
  7: 0x0186 [0x3B] GET_ENTITY_POSITION(entity=LocalPlayer, x_destination=ExtData[1]->WorkLocal[6], y_destination=ExtData[1]->WorkLocal[8], z_destination=ExtData[1]->WorkLocal[7])
  8: 0x0191 [0x3A] CONVERT_YAW_TO_BYTE(entity=LocalPlayer, result_destination=ExtData[1]->WorkLocal[9])
  9: 0x0198 [0x64] CALCULATE_DISTANCE: ExtData[1]->WorkLocal[5] = distance between point1(ExtData[1]->WorkLocal[6], ExtData[1]->WorkLocal[8]) and point2(4294834107*, 133150*)
 10: 0x01A3 [0x02] IF !(ExtData[1]->WorkLocal[5] <= 500*) GOTO 0x01AD
 11: 0x01AB [0x21] END_EVENT
 12: 0x01AC [0x00] END_REQSTACK()
 13: 0x01AD [0x03] ExtData[1]->WorkLocal[14] = ExtData[1]->WorkLocal[6]
 14: 0x01B2 [0x03] ExtData[1]->WorkLocal[16] = ExtData[1]->WorkLocal[8]
 15: 0x01B7 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
 16: 0x01B9 [0x03] ExtData[1]->WorkLocal[4] = 0*
 17: 0x01BE [0x06] ExtData[1]->WorkLocal[3] = 0
 18: 0x01C1 [0x06] ExtData[1]->WorkLocal[2] = 0
 19: 0x01C4 [0x06] ExtData[1]->WorkLocal[5] = 0

SUBROUTINE_01C7:
 20: 0x01C7 [0x02] IF !(ExtData[1]->WorkLocal[5] == 0*) GOTO 0x0293
 21: 0x01CF [0x02] IF !(ExtData[1]->WorkLocal[17] == 0*) GOTO 0x01FB
 22: 0x01D7 [0x17] ExtData[1]->WorkLocal[12] = cos(ExtData[1]->WorkLocal[4]) * 120*
 23: 0x01DE [0x08] ExtData[1]->WorkLocal[12] -= 120*
 24: 0x01E3 [0x08] ExtData[1]->WorkLocal[12] -= 60*
 25: 0x01E8 [0x07] ExtData[1]->WorkLocal[4] += 256*
 26: 0x01ED [0x02] IF !(ExtData[1]->WorkLocal[4] <= 1024*) GOTO 0x01F8
 27: 0x01F5 [0x0B] ExtData[1]->WorkLocal[17]++
 28: 0x01F8 [0x01] GOTO 0x0249
 29: 0x01FB [0x02] IF !(ExtData[1]->WorkLocal[17] == 1*) GOTO 0x0222
 30: 0x0203 [0x17] ExtData[1]->WorkLocal[12] = cos(ExtData[1]->WorkLocal[4]) * 360*
 31: 0x020A [0x08] ExtData[1]->WorkLocal[12] -= 360*
 32: 0x020F [0x07] ExtData[1]->WorkLocal[4] += 256*
 33: 0x0214 [0x02] IF !(ExtData[1]->WorkLocal[4] < 2048*) GOTO 0x021F
 34: 0x021C [0x0B] ExtData[1]->WorkLocal[17]++
 35: 0x021F [0x01] GOTO 0x0249
 36: 0x0222 [0x02] IF !(ExtData[1]->WorkLocal[17] == 2*) GOTO 0x0244
 37: 0x022A [0x17] ExtData[1]->WorkLocal[12] = cos(ExtData[1]->WorkLocal[4]) * 480*
 38: 0x0231 [0x07] ExtData[1]->WorkLocal[4] += 100*
 39: 0x0236 [0x02] IF !(ExtData[1]->WorkLocal[4] < 3584*) GOTO 0x0241
 40: 0x023E [0x0B] ExtData[1]->WorkLocal[17]++
 41: 0x0241 [0x01] GOTO 0x0249
 42: 0x0244 [0x05] ExtData[1]->WorkLocal[5] = 1
 43: 0x0247 [0x33] EventEntity->Render.Flags0 &= ~ 0x200000 // Bit 21 (flag=0x00)

SUBROUTINE_0249:
 44: 0x0249 [0x17] ExtData[1]->WorkLocal[3] = cos(ExtData[1]->WorkLocal[2]) * 800*
 45: 0x0250 [0x08] ExtData[1]->WorkLocal[3] -= 800*
 46: 0x0255 [0x14] ExtData[1]->WorkLocal[3] *= 4294967295*
 47: 0x025A [0x17] ExtData[1]->WorkLocal[10] = cos(2642*) * ExtData[1]->WorkLocal[3]
 48: 0x0261 [0x16] ExtData[1]->WorkLocal[11] = sin(2642*) * ExtData[1]->WorkLocal[3]
 49: 0x0268 [0x02] IF !(ExtData[1]->WorkLocal[2] > 1024*) GOTO 0x0275
 50: 0x0270 [0x07] ExtData[1]->WorkLocal[2] += 32*
 51: 0x0275 [0x07] ExtData[1]->WorkLocal[6] += ExtData[1]->WorkLocal[10]
 52: 0x027A [0x07] ExtData[1]->WorkLocal[8] += ExtData[1]->WorkLocal[11]
 53: 0x027F [0x07] ExtData[1]->WorkLocal[7] += ExtData[1]->WorkLocal[12]
 54: 0x0284 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[6], z=ExtData[1]->WorkLocal[8], y=ExtData[1]->WorkLocal[7], direction=ExtData[1]->WorkLocal[9]
 55: 0x028D [0x1C] WAIT(1* ticks)
 56: 0x0290 [0x01] GOTO 0x01C7
 57: 0x0293 [0x14] ExtData[1]->WorkLocal[10] *= 3*
 58: 0x0298 [0x14] ExtData[1]->WorkLocal[11] *= 3*
 59: 0x029D [0x14] ExtData[1]->WorkLocal[12] *= 3*
 60: 0x02A2 [0x07] ExtData[1]->WorkLocal[6] += ExtData[1]->WorkLocal[10]
 61: 0x02A7 [0x07] ExtData[1]->WorkLocal[8] += ExtData[1]->WorkLocal[11]
 62: 0x02AC [0x07] ExtData[1]->WorkLocal[7] += ExtData[1]->WorkLocal[12]
 63: 0x02B1 [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[6], Z=ExtData[1]->WorkLocal[8], Y=ExtData[1]->WorkLocal[7]
 64: 0x02B9 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 65: 0x02BB [0x21] END_EVENT
 66: 0x02BC [0x00] END_REQSTACK()
```

### Event 11

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x02BD    |
| Data Size    | 282 bytes |
| Instructions | 57        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02B0:                                         42 06 21               B.!
02C0: 00 06 1A 00 06 1B 00 06  1C 00 06 1D 00 3B F0 FF  .............;..
02D0: FF 7F 16 00 18 00 17 00  3A F0 FF FF 7F 19 00 64  ........:......d
02E0: 15 00 16 00 18 00 25 80  26 80 02 15 00 17 80 02  ......%.&.......
02F0: F4 02 21 00 03 1E 00 16  00 03 20 00 18 00 33 01  ..!....... ...3.
0300: 03 14 00 09 80 06 13 00  06 12 00 06 15 00 02 15  ................
0310: 00 09 80 00 D5 03 02 21  00 09 80 80 3D 03 17 1C  .......!....=...
0320: 00 14 00 18 80 08 1C 00  18 80 07 14 00 27 80 02  .............'..
0330: 14 00 1B 80 04 3A 03 0B  21 00 01 8B 03 02 21 00  .....:..!.....!.
0340: 01 80 80 64 03 17 1C 00  14 00 18 80 08 1C 00 18  ...d............
0350: 80 07 14 00 28 80 02 14  00 1D 80 04 61 03 0B 21  ....(.......a..!
0360: 00 01 8B 03 02 21 00 02  80 80 86 03 17 1C 00 14  .....!..........
0370: 00 29 80 07 14 00 27 80  02 14 00 2A 80 04 83 03  .)....'....*....
0380: 0B 21 00 01 8B 03 05 15  00 33 00 17 13 00 12 00  .!.......3......
0390: 17 80 08 13 00 17 80 14  13 00 22 80 17 1A 00 23  .........."....#
03A0: 80 13 00 16 1B 00 23 80  13 00 02 12 00 1B 80 05  ......#.........
03B0: B7 03 07 12 00 2B 80 07  16 00 1A 00 07 18 00 1B  .....+..........
03C0: 00 07 17 00 1C 00 37 16  00 18 00 17 00 19 00 1C  ......7.........
03D0: 01 80 01 0E 03 21 00                              .....!.         
```

#### Opcodes

```
  0: 0x02BD [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x02BE [0x06] ExtData[1]->WorkLocal[33] = 0
  2: 0x02C1 [0x06] ExtData[1]->WorkLocal[26] = 0
  3: 0x02C4 [0x06] ExtData[1]->WorkLocal[27] = 0
  4: 0x02C7 [0x06] ExtData[1]->WorkLocal[28] = 0
  5: 0x02CA [0x06] ExtData[1]->WorkLocal[29] = 0
  6: 0x02CD [0x3B] GET_ENTITY_POSITION(entity=LocalPlayer, x_destination=ExtData[1]->WorkLocal[22], y_destination=ExtData[1]->WorkLocal[24], z_destination=ExtData[1]->WorkLocal[23])
  7: 0x02D8 [0x3A] CONVERT_YAW_TO_BYTE(entity=LocalPlayer, result_destination=ExtData[1]->WorkLocal[25])
  8: 0x02DF [0x64] CALCULATE_DISTANCE: ExtData[1]->WorkLocal[21] = distance between point1(ExtData[1]->WorkLocal[22], ExtData[1]->WorkLocal[24]) and point2(4294754129*, 93238*)
  9: 0x02EA [0x02] IF !(ExtData[1]->WorkLocal[21] <= 500*) GOTO 0x02F4
 10: 0x02F2 [0x21] END_EVENT
 11: 0x02F3 [0x00] END_REQSTACK()
 12: 0x02F4 [0x03] ExtData[1]->WorkLocal[30] = ExtData[1]->WorkLocal[22]
 13: 0x02F9 [0x03] ExtData[1]->WorkLocal[32] = ExtData[1]->WorkLocal[24]
 14: 0x02FE [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
 15: 0x0300 [0x03] ExtData[1]->WorkLocal[20] = 0*
 16: 0x0305 [0x06] ExtData[1]->WorkLocal[19] = 0
 17: 0x0308 [0x06] ExtData[1]->WorkLocal[18] = 0
 18: 0x030B [0x06] ExtData[1]->WorkLocal[21] = 0

SUBROUTINE_030E:
 19: 0x030E [0x02] IF !(ExtData[1]->WorkLocal[21] == 0*) GOTO 0x03D5
 20: 0x0316 [0x02] IF !(ExtData[1]->WorkLocal[33] == 0*) GOTO 0x033D
 21: 0x031E [0x17] ExtData[1]->WorkLocal[28] = cos(ExtData[1]->WorkLocal[20]) * 120*
 22: 0x0325 [0x08] ExtData[1]->WorkLocal[28] -= 120*
 23: 0x032A [0x07] ExtData[1]->WorkLocal[20] += 128*
 24: 0x032F [0x02] IF !(ExtData[1]->WorkLocal[20] < 1024*) GOTO 0x033A
 25: 0x0337 [0x0B] ExtData[1]->WorkLocal[33]++
 26: 0x033A [0x01] GOTO 0x038B
 27: 0x033D [0x02] IF !(ExtData[1]->WorkLocal[33] == 1*) GOTO 0x0364
 28: 0x0345 [0x17] ExtData[1]->WorkLocal[28] = cos(ExtData[1]->WorkLocal[20]) * 120*
 29: 0x034C [0x08] ExtData[1]->WorkLocal[28] -= 120*
 30: 0x0351 [0x07] ExtData[1]->WorkLocal[20] += 64*
 31: 0x0356 [0x02] IF !(ExtData[1]->WorkLocal[20] < 2048*) GOTO 0x0361
 32: 0x035E [0x0B] ExtData[1]->WorkLocal[33]++
 33: 0x0361 [0x01] GOTO 0x038B
 34: 0x0364 [0x02] IF !(ExtData[1]->WorkLocal[33] == 2*) GOTO 0x0386
 35: 0x036C [0x17] ExtData[1]->WorkLocal[28] = cos(ExtData[1]->WorkLocal[20]) * 240*
 36: 0x0373 [0x07] ExtData[1]->WorkLocal[20] += 128*
 37: 0x0378 [0x02] IF !(ExtData[1]->WorkLocal[20] < 4096*) GOTO 0x0383
 38: 0x0380 [0x0B] ExtData[1]->WorkLocal[33]++
 39: 0x0383 [0x01] GOTO 0x038B
 40: 0x0386 [0x05] ExtData[1]->WorkLocal[21] = 1
 41: 0x0389 [0x33] EventEntity->Render.Flags0 &= ~ 0x200000 // Bit 21 (flag=0x00)

SUBROUTINE_038B:
 42: 0x038B [0x17] ExtData[1]->WorkLocal[19] = cos(ExtData[1]->WorkLocal[18]) * 500*
 43: 0x0392 [0x08] ExtData[1]->WorkLocal[19] -= 500*
 44: 0x0397 [0x14] ExtData[1]->WorkLocal[19] *= 4294967295*
 45: 0x039C [0x17] ExtData[1]->WorkLocal[26] = cos(2642*) * ExtData[1]->WorkLocal[19]
 46: 0x03A3 [0x16] ExtData[1]->WorkLocal[27] = sin(2642*) * ExtData[1]->WorkLocal[19]
 47: 0x03AA [0x02] IF !(ExtData[1]->WorkLocal[18] > 1024*) GOTO 0x03B7
 48: 0x03B2 [0x07] ExtData[1]->WorkLocal[18] += 16*
 49: 0x03B7 [0x07] ExtData[1]->WorkLocal[22] += ExtData[1]->WorkLocal[26]
 50: 0x03BC [0x07] ExtData[1]->WorkLocal[24] += ExtData[1]->WorkLocal[27]
 51: 0x03C1 [0x07] ExtData[1]->WorkLocal[23] += ExtData[1]->WorkLocal[28]
 52: 0x03C6 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[22], z=ExtData[1]->WorkLocal[24], y=ExtData[1]->WorkLocal[23], direction=ExtData[1]->WorkLocal[25]
 53: 0x03CF [0x1C] WAIT(1* ticks)
 54: 0x03D2 [0x01] GOTO 0x030E
 55: 0x03D5 [0x21] END_EVENT
 56: 0x03D6 [0x00] END_REQSTACK()
```

### Event 12

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x03D7    |
| Data Size    | 282 bytes |
| Instructions | 57        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03D0:                      42  06 31 00 06 2A 00 06 2B         B.1..*..+
03E0: 00 06 2C 00 06 2D 00 3B  F0 FF FF 7F 26 00 28 00  ..,..-.;....&.(.
03F0: 27 00 3A F0 FF FF 7F 29  00 64 25 00 26 00 28 00  '.:....).d%.&.(.
0400: 2C 80 2D 80 02 25 00 17  80 02 0E 04 21 00 03 2E  ,.-..%......!...
0410: 00 26 00 03 30 00 28 00  33 01 03 24 00 09 80 06  .&..0.(.3..$....
0420: 23 00 06 22 00 06 25 00  02 25 00 09 80 00 EF 04  #.."..%..%......
0430: 02 31 00 09 80 80 57 04  17 2C 00 24 00 18 80 08  .1....W..,.$....
0440: 2C 00 18 80 07 24 00 27  80 02 24 00 1B 80 04 54  ,....$.'..$....T
0450: 04 0B 31 00 01 A5 04 02  31 00 01 80 80 7E 04 17  ..1.....1....~..
0460: 2C 00 24 00 18 80 08 2C  00 18 80 07 24 00 28 80  ,.$....,....$.(.
0470: 02 24 00 1D 80 04 7B 04  0B 31 00 01 A5 04 02 31  .$....{..1.....1
0480: 00 02 80 80 A0 04 17 2C  00 24 00 29 80 07 24 00  .......,.$.)..$.
0490: 27 80 02 24 00 2A 80 04  9D 04 0B 31 00 01 A5 04  '..$.*.....1....
04A0: 05 25 00 33 00 17 23 00  22 00 17 80 08 23 00 17  .%.3..#."....#..
04B0: 80 14 23 00 22 80 17 2A  00 2E 80 23 00 16 2B 00  ..#."..*...#..+.
04C0: 2E 80 23 00 02 22 00 1B  80 05 D1 04 07 22 00 2B  ..#..".......".+
04D0: 80 07 26 00 2A 00 07 28  00 2B 00 07 27 00 2C 00  ..&.*..(.+..'.,.
04E0: 37 26 00 28 00 27 00 29  00 1C 01 80 01 28 04 21  7&.(.'.).....(.!
04F0: 00                                                .               
```

#### Opcodes

```
  0: 0x03D7 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x03D8 [0x06] ExtData[1]->WorkLocal[49] = 0
  2: 0x03DB [0x06] ExtData[1]->WorkLocal[42] = 0
  3: 0x03DE [0x06] ExtData[1]->WorkLocal[43] = 0
  4: 0x03E1 [0x06] ExtData[1]->WorkLocal[44] = 0
  5: 0x03E4 [0x06] ExtData[1]->WorkLocal[45] = 0
  6: 0x03E7 [0x3B] GET_ENTITY_POSITION(entity=LocalPlayer, x_destination=ExtData[1]->WorkLocal[38], y_destination=ExtData[1]->WorkLocal[40], z_destination=ExtData[1]->WorkLocal[39])
  7: 0x03F2 [0x3A] CONVERT_YAW_TO_BYTE(entity=LocalPlayer, result_destination=ExtData[1]->WorkLocal[41])
  8: 0x03F9 [0x64] CALCULATE_DISTANCE: ExtData[1]->WorkLocal[37] = distance between point1(ExtData[1]->WorkLocal[38], ExtData[1]->WorkLocal[40]) and point2(4294900438*, 533309*)
  9: 0x0404 [0x02] IF !(ExtData[1]->WorkLocal[37] <= 500*) GOTO 0x040E
 10: 0x040C [0x21] END_EVENT
 11: 0x040D [0x00] END_REQSTACK()
 12: 0x040E [0x03] ExtData[1]->WorkLocal[46] = ExtData[1]->WorkLocal[38]
 13: 0x0413 [0x03] ExtData[1]->WorkLocal[48] = ExtData[1]->WorkLocal[40]
 14: 0x0418 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
 15: 0x041A [0x03] ExtData[1]->WorkLocal[36] = 0*
 16: 0x041F [0x06] ExtData[1]->WorkLocal[35] = 0
 17: 0x0422 [0x06] ExtData[1]->WorkLocal[34] = 0
 18: 0x0425 [0x06] ExtData[1]->WorkLocal[37] = 0

SUBROUTINE_0428:
 19: 0x0428 [0x02] IF !(ExtData[1]->WorkLocal[37] == 0*) GOTO 0x04EF
 20: 0x0430 [0x02] IF !(ExtData[1]->WorkLocal[49] == 0*) GOTO 0x0457
 21: 0x0438 [0x17] ExtData[1]->WorkLocal[44] = cos(ExtData[1]->WorkLocal[36]) * 120*
 22: 0x043F [0x08] ExtData[1]->WorkLocal[44] -= 120*
 23: 0x0444 [0x07] ExtData[1]->WorkLocal[36] += 128*
 24: 0x0449 [0x02] IF !(ExtData[1]->WorkLocal[36] < 1024*) GOTO 0x0454
 25: 0x0451 [0x0B] ExtData[1]->WorkLocal[49]++
 26: 0x0454 [0x01] GOTO 0x04A5
 27: 0x0457 [0x02] IF !(ExtData[1]->WorkLocal[49] == 1*) GOTO 0x047E
 28: 0x045F [0x17] ExtData[1]->WorkLocal[44] = cos(ExtData[1]->WorkLocal[36]) * 120*
 29: 0x0466 [0x08] ExtData[1]->WorkLocal[44] -= 120*
 30: 0x046B [0x07] ExtData[1]->WorkLocal[36] += 64*
 31: 0x0470 [0x02] IF !(ExtData[1]->WorkLocal[36] < 2048*) GOTO 0x047B
 32: 0x0478 [0x0B] ExtData[1]->WorkLocal[49]++
 33: 0x047B [0x01] GOTO 0x04A5
 34: 0x047E [0x02] IF !(ExtData[1]->WorkLocal[49] == 2*) GOTO 0x04A0
 35: 0x0486 [0x17] ExtData[1]->WorkLocal[44] = cos(ExtData[1]->WorkLocal[36]) * 240*
 36: 0x048D [0x07] ExtData[1]->WorkLocal[36] += 128*
 37: 0x0492 [0x02] IF !(ExtData[1]->WorkLocal[36] < 4096*) GOTO 0x049D
 38: 0x049A [0x0B] ExtData[1]->WorkLocal[49]++
 39: 0x049D [0x01] GOTO 0x04A5
 40: 0x04A0 [0x05] ExtData[1]->WorkLocal[37] = 1
 41: 0x04A3 [0x33] EventEntity->Render.Flags0 &= ~ 0x200000 // Bit 21 (flag=0x00)

SUBROUTINE_04A5:
 42: 0x04A5 [0x17] ExtData[1]->WorkLocal[35] = cos(ExtData[1]->WorkLocal[34]) * 500*
 43: 0x04AC [0x08] ExtData[1]->WorkLocal[35] -= 500*
 44: 0x04B1 [0x14] ExtData[1]->WorkLocal[35] *= 4294967295*
 45: 0x04B6 [0x17] ExtData[1]->WorkLocal[42] = cos(3700*) * ExtData[1]->WorkLocal[35]
 46: 0x04BD [0x16] ExtData[1]->WorkLocal[43] = sin(3700*) * ExtData[1]->WorkLocal[35]
 47: 0x04C4 [0x02] IF !(ExtData[1]->WorkLocal[34] > 1024*) GOTO 0x04D1
 48: 0x04CC [0x07] ExtData[1]->WorkLocal[34] += 16*
 49: 0x04D1 [0x07] ExtData[1]->WorkLocal[38] += ExtData[1]->WorkLocal[42]
 50: 0x04D6 [0x07] ExtData[1]->WorkLocal[40] += ExtData[1]->WorkLocal[43]
 51: 0x04DB [0x07] ExtData[1]->WorkLocal[39] += ExtData[1]->WorkLocal[44]
 52: 0x04E0 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[38], z=ExtData[1]->WorkLocal[40], y=ExtData[1]->WorkLocal[39], direction=ExtData[1]->WorkLocal[41]
 53: 0x04E9 [0x1C] WAIT(1* ticks)
 54: 0x04EC [0x01] GOTO 0x0428
 55: 0x04EF [0x21] END_EVENT
 56: 0x04F0 [0x00] END_REQSTACK()
```

### Event 120

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x04F1   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
04F0:    36 2F 80 30 80 31 80  1E 71 F1 0B 01 00         6/.0.1..q....  
```

#### Opcodes

```
  0: 0x04F1 [0x36] SET_ENTITY_EVENT_POSITION(pos_x=-371.099*, pos_z=228.450*, pos_y=3.956*)
  1: 0x04F8 [0x1E] EventEntity looks at Saltvix (ID: 17559921/0x010BF171) and starts talking
  2: 0x04FD [0x00] END_REQSTACK()
```

### Event 121

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x04FE   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
04F0:                                            36 32                62
0500: 80 33 80 34 80 1E 72 F1  0B 01 00                 .3.4..r....     
```

#### Opcodes

```
  0: 0x04FE [0x36] SET_ENTITY_EVENT_POSITION(pos_x=-376.572*, pos_z=442.199*, pos_y=-0.009*)
  1: 0x0505 [0x1E] EventEntity looks at Grasswix (ID: 17559922/0x010BF172) and starts talking
  2: 0x050A [0x00] END_REQSTACK()
```

### Event 122

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x050B   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0500:                                   36 35 80 36 80             65.6.
0510: 37 80 1E 73 F1 0B 01 00                           7..s....        
```

#### Opcodes

```
  0: 0x050B [0x36] SET_ENTITY_EVENT_POSITION(pos_x=-460.681*, pos_z=-139.291*, pos_y=3.981*)
  1: 0x0512 [0x1E] EventEntity looks at Eggblix (ID: 17559923/0x010BF173) and starts talking
  2: 0x0517 [0x00] END_REQSTACK()
```

### Event 150

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0518    |
| Data Size    | 220 bytes |
| Instructions | 30        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0510:                          42 46 01 22 01 4E 00 76          BF.".N.v
0520: F1 0B 01 4E 00 77 F1 0B  01 80 77 F1 0B 01 80 76  ...N.w....w....v
0530: F1 0B 01 45 38 80 F8 FF  FF 7F F8 FF FF 7F 73 68  ...E8.........sh
0540: 67 30 09 80 55 38 80 F8  FF FF 7F F8 FF FF 7F 73  g0..U8.........s
0550: 68 67 30 45 39 80 F8 FF  FF 7F F8 FF FF 7F 66 64  hg0E9.........fd
0560: 69 32 09 80 55 39 80 F8  FF FF 7F F8 FF FF 7F 66  i2..U9.........f
0570: 64 69 32 4B 76 F1 0B 01  3A 80 6F 76 76 F1 0B 01  di2Kv...:.ovv...
0580: 73 3B 80 77 F1 0B 01 77  F1 0B 01 2B 76 F1 0B 01  s;.w...w...+v...
0590: 3C 80 23 4E 01 77 F1 0B  01 2B 76 F1 0B 01 3D 80  <.#N.w...+v...=.
05A0: 23 4B 76 F1 0B 01 3E 80  45 39 80 F8 FF FF 7F F8  #Kv...>.E9......
05B0: FF FF 7F 66 64 6F 31 09  80 55 39 80 F8 FF FF 7F  ...fdo1..U9.....
05C0: F8 FF FF 7F 66 64 6F 31  4E 01 76 F1 0B 01 22 00  ....fdo1N.v...".
05D0: 46 00 45 39 80 F8 FF FF  7F F8 FF FF 7F 66 64 69  F.E9.........fdi
05E0: 31 09 80 55 39 80 F8 FF  FF 7F F8 FF FF 7F 66 64  1..U9.........fd
05F0: 69 31 21 00                                       i1!.            
```

#### Opcodes

```
  0: 0x0518 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0519 [0x46] CAMERA_CONTROL: Disable user control
  2: 0x051B [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  3: 0x051D [0x4E] SET_ENTITY_HIDE_FLAG: Show Ken (ID: 17559926/0x010BF176)
  4: 0x0523 [0x4E] SET_ENTITY_HIDE_FLAG: Show Marin (ID: 17559927/0x010BF177)
  5: 0x0529 [0x80] LOAD_WAIT(entity=Marin (ID: 17559927/0x010BF177))
  6: 0x052E [0x80] LOAD_WAIT(entity=Ken (ID: 17559926/0x010BF176))
  7: 0x0533 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "shg0" with entities [EventEntity, EventEntity], work=[35*, 0*]
  8: 0x0544 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "shg0" with entities [EventEntity, EventEntity], work=35*
  9: 0x0553 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [EventEntity, EventEntity], work=[200*, 0*]
 10: 0x0564 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi2" with entities [EventEntity, EventEntity], work=200*
 11: 0x0573 [0x4B] UPDATE_ENTITY_YAW(entity=Ken (ID: 17559926/0x010BF176), yaw=20.6°*)
 12: 0x057A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 13: 0x057B [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Ken (ID: 17559926/0x010BF176) Render.Flags0 and Render.Flags3 conditions are met
 14: 0x0580 [0x73] Marin (ID: 17559927/0x010BF177) casts magic 498* on Marin (ID: 17559927/0x010BF177)
 15: 0x058B [0x2B] Ken (ID: 17559926/0x010BF176) [7463*]:
    → "Eh? Don't tell me that you came here to protect me. I told you I'd be fine on my own!"
 16: 0x0592 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x0593 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Marin (ID: 17559927/0x010BF177)
 18: 0x0599 [0x2B] Ken (ID: 17559926/0x010BF176) [7464*]:
    → "Now get out of my face! If I even see you..."
 19: 0x05A0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x05A1 [0x4B] UPDATE_ENTITY_YAW(entity=Ken (ID: 17559926/0x010BF176), yaw=9.2°*)
 21: 0x05A8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 22: 0x05B9 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [EventEntity, EventEntity], work=200*
 23: 0x05C8 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Ken (ID: 17559926/0x010BF176)
 24: 0x05CE [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
 25: 0x05D0 [0x46] CAMERA_CONTROL: Restore default settings
 26: 0x05D2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 27: 0x05E3 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [EventEntity, EventEntity], work=200*
 28: 0x05F2 [0x21] END_EVENT
 29: 0x05F3 [0x00] END_REQSTACK()
```
