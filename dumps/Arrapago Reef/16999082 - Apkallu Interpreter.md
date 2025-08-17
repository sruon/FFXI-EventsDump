# 16999082 - Apkallu Interpreter

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Arrapago Reef (ID: 54) |
| Block Size       | 352 bytes              |
| Total Events     | 16                     |
| References Count | 17                     |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     14 |              2 |
| [65535.2](#event-655352)   | 0x000F       |     14 |              2 |
| [65535.3](#event-655353)   | 0x001D       |     14 |              2 |
| [65535.4](#event-655354)   | 0x002B       |     14 |              2 |
| [65535.5](#event-655355)   | 0x0039       |     13 |              2 |
| [65535.6](#event-655356)   | 0x0046       |     13 |              2 |
| [65535.7](#event-655357)   | 0x0053       |     13 |              2 |
| [243](#event-243)          | 0x0060       |      7 |              2 |
| [244](#event-244)          | 0x0067       |      7 |              2 |
| [248](#event-248)          | 0x006E       |      7 |              2 |
| [65535.8](#event-655358)   | 0x0075       |     14 |              4 |
| [65535.9](#event-655359)   | 0x0083       |     15 |              5 |
| [65535.10](#event-6553510) | 0x0092       |     24 |              6 |
| [250](#event-250)          | 0x00AA       |      7 |              2 |
| [65535.11](#event-6553511) | 0x00B1       |     24 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0489      |        1161 |
|       1 | 0x048B      |        1163 |
|       2 | 0x0488      |        1160 |
|       3 | 0x0028      |          40 |
|       4 | 0xFFF711BF  |  4294382015 |
|       5 | 0x488B4     |      297140 |
|       6 | 0xFFFFE3BD  |  4294960061 |
|       7 | 0x000D      |          13 |
|       8 | 0xFFF70FE6  |  4294381542 |
|       9 | 0x48390     |      295824 |
|      10 | 0xFFFFE580  |  4294960512 |
|      11 | 0xFFF70A0D  |  4294380045 |
|      12 | 0x49BB6     |      302006 |
|      13 | 0xFFFFDE62  |  4294958690 |
|      14 | 0xFFF6F23C  |  4294373948 |
|      15 | 0x4AC12     |      306194 |
|      16 | 0xFFFFDE48  |  4294958664 |

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    2C F8 FF FF 7F F8 FF  FF 7F 73 70 30 31 00      ,........sp01. 
```

#### Opcodes

```
  0: 0x0001 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp01" with entities [EventEntity, EventEntity]
  1: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               53                 S
0010: F8 FF FF 7F F8 FF FF 7F  73 70 30 31 00           ........sp01.   
```

#### Opcodes

```
  0: 0x000F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp01" with entities [EventEntity, EventEntity]
  1: 0x001C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         2C F8 FF               ,..
0020: FF 7F F8 FF FF 7F 73 70  30 32 00                 ......sp02.     
```

#### Opcodes

```
  0: 0x001D [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "sp02" with entities [EventEntity, EventEntity]
  1: 0x002A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   53 F8 FF FF 7F             S....
0030: F8 FF FF 7F 73 70 30 32  00                       ....sp02.       
```

#### Opcodes

```
  0: 0x002B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sp02" with entities [EventEntity, EventEntity]
  1: 0x0038 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 13 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             C4 02 00 80 F8 FF FF           .......
0040: 7F F0 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x0039 [0xC4] SCHEDULE_MAGIC_CASTING_ALT (arg=18): EventEntity casts magic 1161* on LocalPlayer
  1: 0x0045 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0046   |
| Data Size    | 13 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   C4 02  01 80 F8 FF FF 7F F0 FF        ..........
0050: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x0046 [0xC4] SCHEDULE_MAGIC_CASTING_ALT (arg=18): EventEntity casts magic 1163* on LocalPlayer
  1: 0x0052 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0053   |
| Data Size    | 13 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:          C4 02 02 80 F8  FF FF 7F F0 FF FF 7F 00     .............
```

#### Opcodes

```
  0: 0x0053 [0xC4] SCHEDULE_MAGIC_CASTING_ALT (arg=18): EventEntity casts magic 1160* on LocalPlayer
  1: 0x005F [0x00] END_REQSTACK()
```

### Event 243

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0060  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0060 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0066 [0x00] END_REQSTACK()
```

### Event 244

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0067  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      92  01 F8 FF FF 7F 00               .......  
```

#### Opcodes

```
  0: 0x0067 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x006D [0x00] END_REQSTACK()
```

### Event 248

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006E  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                            92 01                ..
0070: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x006E [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0074 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0075   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                32 03 80  5A 00 04 80 05 80 06 80       2..Z.......
0080: 5A 01 00                                          Z..             
```

#### Opcodes

```
  0: 0x0075 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0078 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-585.281*, Z=297.140*, Y=-7.235*
  2: 0x0080 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x0082 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0083   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:          32 07 80 1F 00  08 80 09 80 0A 80 1F 01     2............
0090: 6F 00                                             o.              
```

#### Opcodes

```
  0: 0x0083 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0086 [0x1F] MOVE_ENTITY: EventEntity moves to X=-585.754*, Z=295.824*, Y=-6.784*
  2: 0x008E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0090 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0091 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0092   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:       32 03 80 5A 00 0B  80 0C 80 0D 80 5A 01 5A    2..Z.......Z.Z
00A0: 00 0E 80 0F 80 10 80 5A  01 00                    .......Z..      
```

#### Opcodes

```
  0: 0x0092 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0095 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-587.251*, Z=302.006*, Y=-8.606*
  2: 0x009D [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x009F [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-593.348*, Z=306.194*, Y=-8.632*
  4: 0x00A7 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  5: 0x00A9 [0x00] END_REQSTACK()
```

### Event 250

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00AA  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                92 01 F8 FF FF 7F            ......
00B0: 00                                                .               
```

#### Opcodes

```
  0: 0x00AA [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00B0 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B1   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:    32 03 80 5A 00 0B 80  0C 80 0D 80 5A 01 5A 00   2..Z.......Z.Z.
00C0: 0E 80 0F 80 10 80 5A 01  00                       ......Z..       
```

#### Opcodes

```
  0: 0x00B1 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00B4 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-587.251*, Z=302.006*, Y=-8.606*
  2: 0x00BC [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x00BE [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-593.348*, Z=306.194*, Y=-8.632*
  4: 0x00C6 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  5: 0x00C8 [0x00] END_REQSTACK()
```
