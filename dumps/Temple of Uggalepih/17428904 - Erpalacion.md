# 17428904 - Erpalacion

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Temple of Uggalepih (ID: 159) |
| Block Size       | 396 bytes                     |
| Total Events     | 9                             |
| References Count | 19                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [67](#event-67)          | 0x0001       |     60 |              8 |
| [65535.1](#event-655351) | 0x003D       |     38 |              5 |
| [65535.2](#event-655352) | 0x0063       |     62 |              8 |
| [65535.3](#event-655353) | 0x00A1       |     28 |              4 |
| [65535.4](#event-655354) | 0x00BD       |     12 |              3 |
| [65535.5](#event-655355) | 0x00C9       |     29 |              3 |
| [65535.6](#event-655356) | 0x00E6       |     29 |              3 |
| [65535.7](#event-655357) | 0x0103       |      9 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xC17B      |       49531 |
|       1 | 0xFFFF2810  |  4294912016 |
|       2 | 0x076B      |        1899 |
|       3 | 0x022C      |         556 |
|       4 | 0x0000      |           0 |
|       5 | 0x0001      |           1 |
|       6 | 0x001D      |          29 |
|       7 | 0x0002      |           2 |
|       8 | 0x0078      |         120 |
|       9 | 0x003C      |          60 |
|      10 | 0x00DF      |         223 |
|      11 | 0x000D      |          13 |
|      12 | 0xCAC2      |       51906 |
|      13 | 0xFFFF1EC3  |  4294909635 |
|      14 | 0x07CF      |        1999 |
|      15 | 0x000B      |          11 |
|      16 | 0x98E0      |       39136 |
|      17 | 0xFFFFF381  |  4294964097 |
|      18 | 0x0BFA      |        3066 |

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

### Event 67

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 60 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    33 01 37 00 80 01 80  02 80 03 80 6C F8 FF FF   3.7........l...
0010: 7F 04 80 05 80 80 F8 FF  FF 7F 92 01 F8 FF FF 7F  ................
0020: 66 06 80 F8 FF FF 7F F8  FF FF 7F 73 69 72 30 53  f..........sir0S
0030: F8 FF FF 7F F8 FF FF 7F  73 69 72 30 00           ........sir0.   
```

#### Opcodes

```
  0: 0x0001 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0003 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=49.531*, z=-55.280*, y=1.899*, direction=48.9°*
  2: 0x000C [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0015 [0x80] LOAD_WAIT(entity=EventEntity)
  4: 0x001A [0x92] EventEntity->Render.Flags3 ^= 0x01
  5: 0x0020 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sir0" with entities [EventEntity, EventEntity], work=29*
  6: 0x002F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sir0" with entities [EventEntity, EventEntity]
  7: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 38 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         22 00 62               ".b
0040: 07 80 F8 FF FF 7F F8 FF  FF 7F 6D 61 69 6E 04 80  ..........main..
0050: 1C 08 80 55 07 80 F8 FF  FF 7F F8 FF FF 7F 6D 61  ...U..........ma
0060: 69 6E 00                                          in.             
```

#### Opcodes

```
  0: 0x003D [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x003F [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [EventEntity, EventEntity], work=[2*, 0*]
  2: 0x0050 [0x1C] WAIT(120* ticks)
  3: 0x0053 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "main" with entities [EventEntity, EventEntity], work=2*
  4: 0x0062 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0063   |
| Data Size    | 62 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          66 06 80 F8 FF  FF 7F F8 FF FF 7F 73 68     f..........sh
0070: 61 31 53 F8 FF FF 7F F8  FF FF 7F 73 68 61 31 1C  a1S........sha1.
0080: 09 80 45 0A 80 F0 FF FF  7F F0 FF FF 7F 78 30 30  ..E..........x00
0090: 62 04 80 32 0B 80 1F 00  0C 80 0D 80 0E 80 1F 01  b..2............
00A0: 00                                                .               
```

#### Opcodes

```
  0: 0x0063 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=29*
  1: 0x0072 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [EventEntity, EventEntity]
  2: 0x007F [0x1C] WAIT(60* ticks)
  3: 0x0082 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "x00b" with entities [LocalPlayer, LocalPlayer], work=[223*, 0*]
  4: 0x0093 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  5: 0x0096 [0x1F] MOVE_ENTITY: EventEntity moves to X=51.906*, Z=-57.661*, Y=1.999*
  6: 0x009E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x00A0 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A1   |
| Data Size    | 28 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:    3B AA F1 09 01 00 00  01 00 02 00 3A AA F1 09   ;..........:...
00B0: 01 03 00 37 00 00 01 00  02 00 03 00 00           ...7.........   
```

#### Opcodes

```
  0: 0x00A1 [0x3B] GET_ENTITY_POSITION(entity=Unnamed NPC (ID: 17428906/0x0109F1AA), x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[2])
  1: 0x00AC [0x3A] CONVERT_YAW_TO_BYTE(entity=Unnamed NPC (ID: 17428906/0x0109F1AA), result_destination=ExtData[1]->WorkLocal[3])
  2: 0x00B3 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[0], z=ExtData[1]->WorkLocal[1], y=ExtData[1]->WorkLocal[2], direction=ExtData[1]->WorkLocal[3]
  3: 0x00BC [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BD   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                         22 00 37               ".7
00C0: 0F 80 10 80 11 80 12 80  00                       .........       
```

#### Opcodes

```
  0: 0x00BD [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x00BF [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.011*, z=39.136*, y=-3.199*, direction=269.5°*
  2: 0x00C8 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C9   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                             66 06 80 A8 F1 09 01           f......
00D0: A8 F1 09 01 73 68 61 31  53 A8 F1 09 01 A8 F1 09  ....sha1S.......
00E0: 01 73 68 61 31 00                                 .sha1.          
```

#### Opcodes

```
  0: 0x00C9 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [Erpalacion (ID: 17428904/0x0109F1A8), Erpalacion (ID: 17428904/0x0109F1A8)], work=29*
  1: 0x00D8 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [Erpalacion (ID: 17428904/0x0109F1A8), Erpalacion (ID: 17428904/0x0109F1A8)]
  2: 0x00E5 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E6   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                   66 06  80 F8 FF FF 7F F8 FF FF        f.........
00F0: 7F 74 6C 6B 30 53 F8 FF  FF 7F F8 FF FF 7F 74 6C  .tlk0S........tl
0100: 6B 30 00                                          k0.             
```

#### Opcodes

```
  0: 0x00E6 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
  1: 0x00F5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  2: 0x0102 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0103  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:          5E 69 64 6C 30  1C 09 80 00                 ^idl0....    
```

#### Opcodes

```
  0: 0x0103 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0108 [0x1C] WAIT(60* ticks)
  2: 0x010B [0x00] END_REQSTACK()
```
