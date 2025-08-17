# 16982238 - Salabwahn

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Aht Urhgan Whitegate2 (ID: 50) |
| Block Size       | 208 bytes                      |
| Total Events     | 11                             |
| References Count | 11                             |

## List of Events

| Event ID                  | Entrypoint   |   Size |   Instructions |
|---------------------------|--------------|--------|----------------|
| [65535](#event-65535)     | 0x0000       |      1 |              1 |
| [65535.1](#event-65535-1) | 0x0001       |      1 |              1 |
| [65535.2](#event-65535-2) | 0x0002       |     18 |              4 |
| [65535.3](#event-65535-3) | 0x0014       |     10 |              2 |
| [65535.4](#event-65535-4) | 0x001E       |      9 |              3 |
| [65535.5](#event-65535-5) | 0x0027       |      9 |              3 |
| [65535.6](#event-65535-6) | 0x0030       |     10 |              2 |
| [65535.7](#event-65535-7) | 0x003A       |     10 |              2 |
| [3130](#event-3130)       | 0x0044       |      1 |              1 |
| [65535.8](#event-65535-8) | 0x0045       |     15 |              5 |
| [65535.9](#event-65535-9) | 0x0054       |     17 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x000B      |          11 |
|       4 | 0x032E      |         814 |
|       5 | 0xFFFF3686  |  4294915718 |
|       6 | 0xFFFF996D  |  4294941037 |
|       7 | 0x000D      |          13 |
|       8 | 0x0470      |        1136 |
|       9 | 0xFFFF3EFA  |  4294917882 |
|      10 | 0xFFFF9977  |  4294941047 |

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

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       22 00 2F 00 F8 FF  FF 7F 6C F8 FF FF 7F 00    "./.....l.....
0010: 80 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0002 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0004 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x000A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0013 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0014   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             6C F8 FF FF  7F 02 80 01 80 00            l.........  
```

#### Opcodes

```
  0: 0x0014 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            22 00                ".
0020: 2F 00 F8 FF FF 7F 00                              /......         
```

#### Opcodes

```
  0: 0x001E [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0020 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      22  01 2F 01 F8 FF FF 7F 00         "./......
```

#### Opcodes

```
  0: 0x0027 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0029 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 6C F8 FF FF 7F 00 80 01  80 00                    l.........      
```

#### Opcodes

```
  0: 0x0030 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0039 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                6C F8 FF FF 7F 02            l.....
0040: 80 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x003A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0043 [0x00] END_REQSTACK()
```

### Event 3130

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0044  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             00                                        .           
```

#### Opcodes

```
  0: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                32 03 80  1F 00 04 80 05 80 06 80       2..........
0050: 1F 01 6F 00                                       ..o.            
```

#### Opcodes

```
  0: 0x0045 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x0048 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.814*, Z=-51.578*, Y=-26.259*
  2: 0x0050 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0052 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0053 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0054   |
| Data Size    | 17 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             32 07 80 1F  00 08 80 09 80 0A 80 1F      2...........
0060: 01 6F 22 01 00                                    .o"..           
```

#### Opcodes

```
  0: 0x0054 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0057 [0x1F] MOVE_ENTITY: EventEntity moves to X=1.136*, Z=-49.414*, Y=-26.249*
  2: 0x005F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0061 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0062 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  5: 0x0064 [0x00] END_REQSTACK()
```
