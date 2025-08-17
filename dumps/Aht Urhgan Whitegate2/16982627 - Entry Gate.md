# 16982627 - Entry Gate

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Aht Urhgan Whitegate2 (ID: 50) |
| Block Size       | 168 bytes                      |
| Total Events     | 12                             |
| References Count | 5                              |

## List of Events

| Event ID                    | Entrypoint   |   Size |   Instructions |
|-----------------------------|--------------|--------|----------------|
| [65535](#event-65535)       | 0x0000       |      1 |              1 |
| [934](#event-934)           | 0x0001       |      1 |              1 |
| [65535.1](#event-65535-1)   | 0x0002       |      2 |              2 |
| [65535.2](#event-65535-2)   | 0x0004       |      2 |              2 |
| [65535.3](#event-65535-3)   | 0x0006       |      9 |              5 |
| [65535.4](#event-65535-4)   | 0x000F       |      1 |              1 |
| [65535.5](#event-65535-5)   | 0x0010       |     18 |              4 |
| [65535.6](#event-65535-6)   | 0x0022       |     10 |              2 |
| [65535.7](#event-65535-7)   | 0x002C       |      9 |              3 |
| [65535.8](#event-65535-8)   | 0x0035       |      9 |              3 |
| [65535.9](#event-65535-9)   | 0x003E       |     10 |              2 |
| [65535.10](#event-65535-10) | 0x0048       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0258      |         600 |
|       1 | 0x001E      |          30 |
|       2 | 0x0000      |           0 |
|       3 | 0x0001      |           1 |
|       4 | 0x0080      |         128 |

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

### Event 934

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       4C 00                                         L.            
```

#### Opcodes

```
  0: 0x0002 [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x0003 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0004  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             4D 00                                     M.          
```

#### Opcodes

```
  0: 0x0004 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0005 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0006  |
| Data Size    | 9 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   4C 1C  00 80 4D 1C 01 80 00           L...M.... 
```

#### Opcodes

```
  0: 0x0006 [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x0007 [0x1C] WAIT(600* ticks)
  2: 0x000A [0x4D] EventEntity->StatusEvent = 9 // Close door
  3: 0x000B [0x1C] WAIT(30* ticks)
  4: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               00                 .
```

#### Opcodes

```
  0: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 22 00 2F 00 F8 FF FF 7F  6C F8 FF FF 7F 02 80 03  "./.....l.......
0020: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0010 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0012 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0018 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0021 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0022   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       6C F8 FF FF 7F 04  80 03 80 00                l.........    
```

#### Opcodes

```
  0: 0x0022 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x002B [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002C  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      22 00 2F 00              "./.
0030: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x002C [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x002E [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0034 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0035  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                22 01 2F  01 F8 FF FF 7F 00             "./......  
```

#### Opcodes

```
  0: 0x0035 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0037 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x003D [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            6C F8                l.
0040: FF FF 7F 02 80 03 80 00                           ........        
```

#### Opcodes

```
  0: 0x003E [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0047 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          6C F8 FF FF 7F 04 80 03          l.......
0050: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0048 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0051 [0x00] END_REQSTACK()
```
