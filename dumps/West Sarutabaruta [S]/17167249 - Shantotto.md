# 17167249 - Shantotto

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | West Sarutabaruta [S] (ID: 95) |
| Block Size       | 256 bytes                      |
| Total Events     | 13                             |
| References Count | 12                             |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [110](#event-110)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     24 |              6 |
| [65535.2](#event-655352)   | 0x001A       |     24 |              6 |
| [65535.3](#event-655353)   | 0x0032       |     10 |              2 |
| [65535.4](#event-655354)   | 0x003C       |     10 |              2 |
| [65535.5](#event-655355)   | 0x0046       |      1 |              1 |
| [65535.6](#event-655356)   | 0x0047       |     18 |              4 |
| [65535.7](#event-655357)   | 0x0059       |     10 |              2 |
| [65535.8](#event-655358)   | 0x0063       |      9 |              3 |
| [65535.9](#event-655359)   | 0x006C       |      9 |              3 |
| [65535.10](#event-6553510) | 0x0075       |     10 |              2 |
| [65535.11](#event-6553511) | 0x007F       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x002B      |          43 |
|       1 | 0xFFFB63BF  |  4294665151 |
|       2 | 0xFFFFCEB4  |  4294954676 |
|       3 | 0xFFFF4480  |  4294919296 |
|       4 | 0xFFFB45AD  |  4294657453 |
|       5 | 0xFFFFCD67  |  4294954343 |
|       6 | 0x0036      |          54 |
|       7 | 0xFFFB8FD0  |  4294676432 |
|       8 | 0xFFFFCE29  |  4294954537 |
|       9 | 0x0000      |           0 |
|      10 | 0x0001      |           1 |
|      11 | 0x0080      |         128 |

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

### Event 110

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
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 1F    2.............
0010: 00 04 80 05 80 03 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 43* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=-302.145*, Z=-12.620*, Y=-48.000*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x1F] MOVE_ENTITY: EventEntity moves to X=-309.843*, Z=-12.953*, Y=-48.000*
  4: 0x0017 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                32 06 80 1F 00 01            2.....
0020: 80 02 80 03 80 1F 01 1F  00 07 80 08 80 03 80 1F  ................
0030: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x001A [0x32] ExtData[1]->MainSpeed = 54* * 0.1
  1: 0x001D [0x1F] MOVE_ENTITY: EventEntity moves to X=-302.145*, Z=-12.620*, Y=-48.000*
  2: 0x0025 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0027 [0x1F] MOVE_ENTITY: EventEntity moves to X=-290.864*, Z=-12.759*, Y=-48.000*
  4: 0x002F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0031 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0032   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       6C F8 FF FF 7F 09  80 0A 80 00                l.........    
```

#### Opcodes

```
  0: 0x0032 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x003B [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003C   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      6C F8 FF FF              l...
0040: 7F 0B 80 0A 80 00                                 ......          
```

#### Opcodes

```
  0: 0x003C [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0045 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0046  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   00                                    .         
```

#### Opcodes

```
  0: 0x0046 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0047   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      22  00 2F 00 F8 FF FF 7F 6C         "./.....l
0050: F8 FF FF 7F 09 80 0A 80  00                       .........       
```

#### Opcodes

```
  0: 0x0047 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0049 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x004F [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0058 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0059   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                             6C F8 FF FF 7F 0B 80           l......
0060: 0A 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0059 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0062 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0063  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          22 00 2F 00 F8  FF FF 7F 00                 "./......    
```

#### Opcodes

```
  0: 0x0063 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0065 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x006B [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006C  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                      22 01 2F 01              "./.
0070: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x006C [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x006E [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x0074 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0075   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                6C F8 FF  FF 7F 09 80 0A 80 00          l......... 
```

#### Opcodes

```
  0: 0x0075 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x007E [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007F   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               6C                 l
0080: F8 FF FF 7F 0B 80 0A 80  00                       .........       
```

#### Opcodes

```
  0: 0x007F [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0088 [0x00] END_REQSTACK()
```
