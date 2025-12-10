# 17207830 - Rochefogne

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Batallia Downs (ID: 105) |
| Block Size       | 444 bytes                |
| Total Events     | 11                       |
| References Count | 21                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [904](#event-904)        | 0x0001       |     22 |              4 |
| [65535.1](#event-655351) | 0x0017       |     15 |              5 |
| [65535.2](#event-655352) | 0x0026       |     58 |             10 |
| [65535.3](#event-655353) | 0x0060       |     15 |              3 |
| [65535.4](#event-655354) | 0x006F       |     29 |              3 |
| [65535.5](#event-655355) | 0x008C       |     29 |              3 |
| [65535.6](#event-655356) | 0x00A9       |     29 |              3 |
| [65535.7](#event-655357) | 0x00C6       |     29 |              3 |
| [65535.8](#event-655358) | 0x00E3       |     40 |              5 |
| [65535.9](#event-655359) | 0x010B       |     31 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x324E7     |      206055 |
|       1 | 0xFFF6D569  |  4294366569 |
|       2 | 0x3BF4      |       15348 |
|       3 | 0x02A4      |         676 |
|       4 | 0x000D      |          13 |
|       5 | 0x32DA2     |      208290 |
|       6 | 0xFFF6C84C  |  4294363212 |
|       7 | 0x3A4D      |       14925 |
|       8 | 0x33B79     |      211833 |
|       9 | 0xFFF6C87F  |  4294363263 |
|      10 | 0x374F      |       14159 |
|      11 | 0x34B20     |      215840 |
|      12 | 0xFFF6C667  |  4294362727 |
|      13 | 0x33FD      |       13309 |
|      14 | 0x00E1      |         225 |
|      15 | 0x0018      |          24 |
|      16 | 0x36757     |      223063 |
|      17 | 0xFFF6D031  |  4294365233 |
|      18 | 0x33F4      |       13300 |
|      19 | 0x08B9      |        2233 |
|      20 | 0x000E      |          14 |

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

### Event 904

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    37 00 80 01 80 02 80  03 80 79 00 F8 FF FF 7F   7........y.....
0010: F0 FF FF 7F A4 01 00                              .......         
```

#### Opcodes

```
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=206.055*, z=-600.727*, y=15.348*, direction=59.4°*
  1: 0x000A [0x79] EventEntity looks at LocalPlayer (Basic look)
  2: 0x0014 [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  3: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      32  04 80 1F 00 05 80 06 80         2........
0020: 07 80 1F 01 6F 00                                 ....o.          
```

#### Opcodes

```
  0: 0x0017 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001A [0x1F] MOVE_ENTITY: EventEntity moves to X=208.290*, Z=-604.084*, Y=14.925*
  2: 0x0022 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0024 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 58 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   1F 00  08 80 09 80 0A 80 1F 01        ..........
0030: 4A 1C 92 06 01 F8 FF FF  7F 4A F0 FF FF 7F F8 FF  J........J......
0040: FF 7F 1F 00 0B 80 0C 80  0D 80 1F 01 6F 4A 1C 92  ............oJ..
0050: 06 01 F8 FF FF 7F 4A F0  FF FF 7F F8 FF FF 7F 00  ......J.........
```

#### Opcodes

```
  0: 0x0026 [0x1F] MOVE_ENTITY: EventEntity moves to X=211.833*, Z=-604.033*, Y=14.159*
  1: 0x002E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0030 [0x4A] Eideialc (ID: 17207836/0x0106921C) looks at EventEntity
  3: 0x0039 [0x4A] LocalPlayer looks at EventEntity
  4: 0x0042 [0x1F] MOVE_ENTITY: EventEntity moves to X=215.840*, Z=-604.569*, Y=13.309*
  5: 0x004A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x004C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x004D [0x4A] Eideialc (ID: 17207836/0x0106921C) looks at EventEntity
  8: 0x0056 [0x4A] LocalPlayer looks at EventEntity
  9: 0x005F [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0060   |
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060: 37 0B 80 0C 80 0D 80 0E  80 1E 18 92 06 01 00     7.............. 
```

#### Opcodes

```
  0: 0x0060 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=215.840*, z=-604.569*, y=13.309*, direction=19.8°*
  1: 0x0069 [0x1E] EventEntity looks at Coteaulepoint (ID: 17207832/0x01069218) and starts talking
  2: 0x006E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006F   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                               66                 f
0070: 0F 80 F8 FF FF 7F F8 FF  FF 7F 31 72 64 79 53 F8  ..........1rdyS.
0080: FF FF 7F F8 FF FF 7F 31  72 64 79 00              .......1rdy.    
```

#### Opcodes

```
  0: 0x006F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "1rdy" with entities [EventEntity, EventEntity], work=24*
  1: 0x007E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "1rdy" with entities [EventEntity, EventEntity]
  2: 0x008B [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008C   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                      66 0F 80 F8              f...
0090: FF FF 7F F8 FF FF 7F 31  72 74 6E 53 F8 FF FF 7F  .......1rtnS....
00A0: F8 FF FF 7F 31 72 74 6E  00                       ....1rtn.       
```

#### Opcodes

```
  0: 0x008C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "1rtn" with entities [EventEntity, EventEntity], work=24*
  1: 0x009B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "1rtn" with entities [EventEntity, EventEntity]
  2: 0x00A8 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A9   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                             5B 04 80 F8 FF FF 7F           [......
00B0: F8 FF FF 7F 74 62 73 30  53 F8 FF FF 7F F8 FF FF  ....tbs0S.......
00C0: 7F 74 62 73 30 00                                 .tbs0.          
```

#### Opcodes

```
  0: 0x00A9 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tbs0" with entities [EventEntity, EventEntity], work=13*
  1: 0x00B8 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tbs0" with entities [EventEntity, EventEntity]
  2: 0x00C5 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C6   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                   5B 04  80 F8 FF FF 7F F8 FF FF        [.........
00D0: 7F 74 62 73 31 53 F8 FF  FF 7F F8 FF FF 7F 74 62  .tbs1S........tb
00E0: 73 31 00                                          s1.             
```

#### Opcodes

```
  0: 0x00C6 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tbs1" with entities [EventEntity, EventEntity], work=13*
  1: 0x00D5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tbs1" with entities [EventEntity, EventEntity]
  2: 0x00E2 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E3   |
| Data Size    | 40 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:          33 01 37 10 80  11 80 12 80 13 80 5B 14     3.7........[.
00F0: 80 F8 FF FF 7F F8 FF FF  7F 66 61 6C 30 53 F8 FF  .........fal0S..
0100: FF 7F F8 FF FF 7F 66 61  6C 30 00                 ......fal0.     
```

#### Opcodes

```
  0: 0x00E3 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x00E5 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=223.063*, z=-602.063*, y=13.300*, direction=196.3°*
  2: 0x00EE [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "fal0" with entities [EventEntity, EventEntity], work=14*
  3: 0x00FD [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "fal0" with entities [EventEntity, EventEntity]
  4: 0x010A [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010B   |
| Data Size    | 31 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                   5B 14 80 F8 FF             [....
0110: FF 7F F8 FF FF 7F 66 61  6C 31 53 F8 FF FF 7F F8  ......fal1S.....
0120: FF FF 7F 66 61 6C 31 22  01 00                    ...fal1"..      
```

#### Opcodes

```
  0: 0x010B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "fal1" with entities [EventEntity, EventEntity], work=14*
  1: 0x011A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "fal1" with entities [EventEntity, EventEntity]
  2: 0x0127 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  3: 0x0129 [0x00] END_REQSTACK()
```
