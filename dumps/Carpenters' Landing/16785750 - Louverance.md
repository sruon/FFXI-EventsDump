# 16785750 - Louverance

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Carpenters' Landing (ID: 2) |
| Block Size       | 676 bytes                   |
| Total Events     | 15                          |
| References Count | 30                          |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [37](#event-37)            | 0x0001       |     49 |              8 |
| [65535.1](#event-655351)   | 0x0032       |     14 |              4 |
| [65535.2](#event-655352)   | 0x0040       |     19 |              5 |
| [65535.3](#event-655353)   | 0x0053       |     25 |              5 |
| [65535.4](#event-655354)   | 0x006C       |     28 |              8 |
| [0](#event-0)              | 0x0088       |     42 |              6 |
| [65535.5](#event-655355)   | 0x00B2       |     24 |              6 |
| [65535.6](#event-655356)   | 0x00CA       |     43 |              7 |
| [65535.7](#event-655357)   | 0x00F5       |     26 |              6 |
| [65535.8](#event-655358)   | 0x010F       |     36 |              4 |
| [65535.9](#event-655359)   | 0x0133       |     16 |              2 |
| [65535.10](#event-6553510) | 0x0143       |     29 |              3 |
| [65535.11](#event-6553511) | 0x0160       |     29 |              3 |
| [65535.12](#event-6553512) | 0x017D       |     97 |             15 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1DDAE     |      122286 |
|       1 | 0xFFF9E7B0  |  4294567856 |
|       2 | 0xFFFFE8D0  |  4294961360 |
|       3 | 0x0B4F      |        2895 |
|       4 | 0xFFFFF448  |  4294964296 |
|       5 | 0x000D      |          13 |
|       6 | 0x0BB8      |        3000 |
|       7 | 0x0028      |          40 |
|       8 | 0x1E28F     |      123535 |
|       9 | 0xFFF9D1CE  |  4294562254 |
|      10 | 0xFFFFE88E  |  4294961294 |
|      11 | 0x1B322     |      111394 |
|      12 | 0xFFF96038  |  4294533176 |
|      13 | 0xFFFFEA39  |  4294961721 |
|      14 | 0xFFFE1677  |  4294841975 |
|      15 | 0xFFF8BEA2  |  4294491810 |
|      16 | 0xFFFFE8EA  |  4294961386 |
|      17 | 0x0E18      |        3608 |
|      18 | 0x019F      |         415 |
|      19 | 0xFFFE21BF  |  4294844863 |
|      20 | 0xFFF8CB22  |  4294495010 |
|      21 | 0xFFFFE948  |  4294961480 |
|      22 | 0xFFFE2363  |  4294845283 |
|      23 | 0xFFF8CF81  |  4294496129 |
|      24 | 0xFFFFE981  |  4294961537 |
|      25 | 0x00A0      |         160 |
|      26 | 0x0078      |         120 |
|      27 | 0x004A      |          74 |
|      28 | 0x0000      |           0 |
|      29 | 0x001D      |          29 |

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

### Event 37

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 49 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    94 01 F8 FF FF 7F 92  01 F8 FF FF 7F 37 00 80   ............7..
0010: 01 80 02 80 03 80 03 04  00 04 80 1A 9A 01 37 05  ..............7.
0020: 00 06 00 07 00 08 00 79  00 F8 FF FF 7F F0 FF FF  .......y........
0030: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x0001 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=122.286*, z=-399.440*, y=-5.936*, direction=254.4°*
  3: 0x0016 [0x03] ExtData[1]->WorkLocal[4] = 4294964296*
  4: 0x001B [0x1A] CALL_SUBROUTINE(address=0x019A)
  5: 0x001E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[5], z=ExtData[1]->WorkLocal[6], y=ExtData[1]->WorkLocal[7], direction=ExtData[1]->WorkLocal[8]
  6: 0x0027 [0x79] EventEntity looks at LocalPlayer (Basic look)
  7: 0x0031 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0032   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       32 05 80 1F 00 00  80 01 80 02 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0032 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0035 [0x1F] MOVE_ENTITY: EventEntity moves to X=122.286*, Z=-399.440*, Y=-5.936*
  2: 0x003D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0040   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040: 03 04 00 06 80 1A 9A 01  1F 00 05 00 06 00 07 00  ................
0050: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0040 [0x03] ExtData[1]->WorkLocal[4] = 3000*
  1: 0x0045 [0x1A] CALL_SUBROUTINE(address=0x019A)
  2: 0x0048 [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[5], Z=ExtData[1]->WorkLocal[6], Y=ExtData[1]->WorkLocal[7]
  3: 0x0050 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0052 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0053   |
| Data Size    | 25 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:          37 00 80 01 80  02 80 03 80 03 04 00 06     7............
0060: 80 1A 9A 01 36 05 00 06  00 07 00 00              ....6.......    
```

#### Opcodes

```
  0: 0x0053 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=122.286*, z=-399.440*, y=-5.936*, direction=254.4°*
  1: 0x005C [0x03] ExtData[1]->WorkLocal[4] = 3000*
  2: 0x0061 [0x1A] CALL_SUBROUTINE(address=0x019A)
  3: 0x0064 [0x36] SET_ENTITY_EVENT_POSITION(pos_x=ExtData[1]->WorkLocal[5], pos_z=ExtData[1]->WorkLocal[6], pos_y=ExtData[1]->WorkLocal[7])
  4: 0x006B [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006C   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                      32 07 80 1F              2...
0070: 00 08 80 09 80 0A 80 1F  01 AB 07 1F 00 0B 80 0C  ................
0080: 80 0D 80 1F 01 22 01 00                           ....."..        
```

#### Opcodes

```
  0: 0x006C [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x006F [0x1F] MOVE_ENTITY: EventEntity moves to X=123.535*, Z=-405.042*, Y=-6.002*
  2: 0x0077 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0079 [0xAB] EventEntity->Render.Flags2 |= 0x01 // Set bit 0
  4: 0x007B [0x1F] MOVE_ENTITY: EventEntity moves to X=111.394*, Z=-434.120*, Y=-5.575*
  5: 0x0083 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0085 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  7: 0x0087 [0x00] END_REQSTACK()
```

### Event 0

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0088   |
| Data Size    | 42 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                          94 01 F8 FF FF 7F 92 01          ........
0090: F8 FF FF 7F 37 0E 80 0F  80 10 80 11 80 80 F8 FF  ....7...........
00A0: FF 7F 5B 12 80 F8 FF FF  7F F8 FF FF 7F 63 68 30  ..[..........ch0
00B0: 32 00                                             2.              
```

#### Opcodes

```
  0: 0x0088 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x008E [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0094 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-125.321*, z=-475.486*, y=-5.910*, direction=317.1°*
  3: 0x009D [0x80] LOAD_WAIT(entity=EventEntity)
  4: 0x00A2 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ch02" with entities [EventEntity, EventEntity], work=415*
  5: 0x00B1 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B2   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:       32 05 80 1F 00 13  80 14 80 15 80 1F 01 1F    2.............
00C0: 00 16 80 17 80 18 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x00B2 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00B5 [0x1F] MOVE_ENTITY: EventEntity moves to X=-122.433*, Z=-472.286*, Y=-5.816*
  2: 0x00BD [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00BF [0x1F] MOVE_ENTITY: EventEntity moves to X=-122.013*, Z=-471.167*, Y=-5.759*
  4: 0x00C7 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00C9 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CA   |
| Data Size    | 43 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                32 05 80 31 00 0E            2..1..
00D0: 80 0F 80 10 80 19 80 31  01 3B 5A 21 00 01 00 00  .......1.;Z!....
00E0: 01 00 02 00 3A 5A 21 00  01 03 00 37 00 00 01 00  ....:Z!....7....
00F0: 02 00 03 00 00                                    .....           
```

#### Opcodes

```
  0: 0x00CA [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00CD [0x31] UPDATE_ENTITY_POSITION: Set EventEntity goal position to X=-125.321*, Z=-475.486*, Y=-5.910*, Time=160*
  2: 0x00D7 [0x31] UPDATE_ENTITY_POSITION: Move EventEntity towards goal position
  3: 0x00D9 [0x3B] GET_ENTITY_POSITION(entity=Chocobo (ID: 16785754/0x0100215A), x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[2])
  4: 0x00E4 [0x3A] CONVERT_YAW_TO_BYTE(entity=Chocobo (ID: 16785754/0x0100215A), result_destination=ExtData[1]->WorkLocal[3])
  5: 0x00EB [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[0], z=ExtData[1]->WorkLocal[1], y=ExtData[1]->WorkLocal[2], direction=ExtData[1]->WorkLocal[3]
  6: 0x00F4 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F5   |
| Data Size    | 26 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                5B 12 80  F8 FF FF 7F F8 FF FF 7F       [..........
0100: 63 68 30 31 1C 1A 80 1E  55 21 00 01 6F 70 00     ch01....U!..op. 
```

#### Opcodes

```
  0: 0x00F5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ch01" with entities [EventEntity, EventEntity], work=415*
  1: 0x0104 [0x1C] WAIT(120* ticks)
  2: 0x0107 [0x1E] EventEntity looks at Guilloud (ID: 16785749/0x01002155) and starts talking
  3: 0x010C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x010D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x010E [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010F   |
| Data Size    | 36 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                               5B                 [
0110: 12 80 F8 FF FF 7F F8 FF  FF 7F 63 68 30 30 1C 19  ..........ch00..
0120: 80 45 1B 80 55 21 00 01  55 21 00 01 73 30 39 30  .E..U!..U!..s090
0130: 1C 80 00                                          ...             
```

#### Opcodes

```
  0: 0x010F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ch00" with entities [EventEntity, EventEntity], work=415*
  1: 0x011E [0x1C] WAIT(160* ticks)
  2: 0x0121 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s090" with entities [Guilloud (ID: 16785749/0x01002155), Guilloud (ID: 16785749/0x01002155)], work=[74*, 0*]
  3: 0x0132 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0133   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:          66 1D 80 F8 FF  FF 7F F8 FF FF 7F 74 6C     f..........tl
0140: 6B 30 00                                          k0.             
```

#### Opcodes

```
  0: 0x0133 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
  1: 0x0142 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0143   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:          66 1D 80 F8 FF  FF 7F F8 FF FF 7F 74 6C     f..........tl
0150: 6B 31 53 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 31 00  k1S........tlk1.
```

#### Opcodes

```
  0: 0x0143 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=29*
  1: 0x0152 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  2: 0x015F [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0160   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160: 66 1D 80 F8 FF FF 7F F8  FF FF 7F 74 68 6B 31 53  f..........thk1S
0170: F8 FF FF 7F F8 FF FF 7F  74 68 6B 31 00           ........thk1.   
```

#### Opcodes

```
  0: 0x0160 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=29*
  1: 0x016F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  2: 0x017C [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x017D   |
| Data Size    | 97 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                         66 1D 80               f..
0180: F8 FF FF 7F F8 FF FF 7F  74 68 6B 32 53 F8 FF FF  ........thk2S...
0190: 7F F8 FF FF 7F 74 68 6B  32 00 3B F8 FF FF 7F 05  .....thk2.;.....
01A0: 00 06 00 07 00 3A F8 FF  FF 7F 08 00 17 09 00 08  .....:..........
01B0: 00 04 00 16 0A 00 08 00  04 00 07 05 00 09 00 07  ................
01C0: 06 00 0A 00 1B 17 09 00  08 00 04 00 16 0A 00 08  ................
01D0: 00 04 00 07 05 00 09 00  07 06 00 0A 00 1B        ..............  
```

#### Opcodes

```
  0: 0x017D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=29*
  1: 0x018C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  2: 0x0199 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x019A [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[5], y_destination=ExtData[1]->WorkLocal[6], z_destination=ExtData[1]->WorkLocal[7])
     0x01A5 [0x3A] CONVERT_YAW_TO_BYTE(entity=EventEntity, result_destination=ExtData[1]->WorkLocal[8])
     0x01AC [0x17] ExtData[1]->WorkLocal[9] = cos(ExtData[1]->WorkLocal[8]) * ExtData[1]->WorkLocal[4]
     0x01B3 [0x16] ExtData[1]->WorkLocal[10] = sin(ExtData[1]->WorkLocal[8]) * ExtData[1]->WorkLocal[4]
     0x01BA [0x07] ExtData[1]->WorkLocal[5] += ExtData[1]->WorkLocal[9]
     0x01BF [0x07] ExtData[1]->WorkLocal[6] += ExtData[1]->WorkLocal[10]
     0x01C4 [0x1B] RETURN
     0x01C5 [0x17] ExtData[1]->WorkLocal[9] = cos(ExtData[1]->WorkLocal[8]) * ExtData[1]->WorkLocal[4]
     0x01CC [0x16] ExtData[1]->WorkLocal[10] = sin(ExtData[1]->WorkLocal[8]) * ExtData[1]->WorkLocal[4]
     0x01D3 [0x07] ExtData[1]->WorkLocal[5] += ExtData[1]->WorkLocal[9]
     0x01D8 [0x07] ExtData[1]->WorkLocal[6] += ExtData[1]->WorkLocal[10]
     0x01DD [0x1B] RETURN
```
