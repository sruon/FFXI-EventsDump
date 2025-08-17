# 17122246 - Lilisette

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Batallia Downs [S] (ID: 84) |
| Block Size       | 292 bytes                   |
| Total Events     | 13                          |
| References Count | 20                          |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |      1 |              1 |
| [65535.2](#event-655352)   | 0x0002       |     18 |              4 |
| [65535.3](#event-655353)   | 0x0014       |     10 |              2 |
| [65535.4](#event-655354)   | 0x001E       |      9 |              3 |
| [65535.5](#event-655355)   | 0x0027       |      9 |              3 |
| [65535.6](#event-655356)   | 0x0030       |     10 |              2 |
| [65535.7](#event-655357)   | 0x003A       |     10 |              2 |
| [3](#event-3)              | 0x0044       |      4 |              2 |
| [65535.8](#event-655358)   | 0x0048       |     34 |              8 |
| [65535.9](#event-655359)   | 0x006A       |     24 |              6 |
| [65535.10](#event-6553510) | 0x0082       |      8 |              3 |
| [65535.11](#event-6553511) | 0x008A       |      6 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x0028      |          40 |
|       4 | 0xFFFEA335  |  4294878005 |
|       5 | 0xFFFD7DB2  |  4294802866 |
|       6 | 0xFFFFED72  |  4294962546 |
|       7 | 0xFFFEAC86  |  4294880390 |
|       8 | 0xFFFD8650  |  4294805072 |
|       9 | 0xFFFFE891  |  4294961297 |
|      10 | 0xFFFEBE79  |  4294884985 |
|      11 | 0xFFFD9F49  |  4294811465 |
|      12 | 0xFFFEAC99  |  4294880409 |
|      13 | 0xFFFD836F  |  4294804335 |
|      14 | 0xFFFEA609  |  4294878729 |
|      15 | 0xFFFD7892  |  4294801554 |
|      16 | 0xFFFFEF66  |  4294963046 |
|      17 | 0x0346      |         838 |
|      18 | 0x0002      |           2 |
|      19 | 0x08E7      |        2279 |

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

### Event 3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0044  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             C0 01 80 00                               ....        
```

#### Opcodes

```
  0: 0x0044 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  1: 0x0047 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 34 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          32 03 80 1F 00 04 80 05          2.......
0050: 80 06 80 1F 01 1F 00 07  80 08 80 09 80 1F 01 1F  ................
0060: 00 0A 80 0B 80 09 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x0048 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x004B [0x1F] MOVE_ENTITY: EventEntity moves to X=-89.291*, Z=-164.430*, Y=-4.750*
  2: 0x0053 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0055 [0x1F] MOVE_ENTITY: EventEntity moves to X=-86.906*, Z=-162.224*, Y=-5.999*
  4: 0x005D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x005F [0x1F] MOVE_ENTITY: EventEntity moves to X=-82.311*, Z=-155.831*, Y=-5.999*
  6: 0x0067 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0069 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006A   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                32 03 80 1F 00 0C            2.....
0070: 80 0D 80 09 80 1F 01 1F  00 0E 80 0F 80 10 80 1F  ................
0080: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x006A [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x006D [0x1F] MOVE_ENTITY: EventEntity moves to X=-86.887*, Z=-162.961*, Y=-5.999*
  2: 0x0075 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0077 [0x1F] MOVE_ENTITY: EventEntity moves to X=-88.567*, Z=-165.742*, Y=-4.250*
  4: 0x007F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0081 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0082  |
| Data Size    | 8 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:       B6 00 11 80 95 12  80 00                      ........      
```

#### Opcodes

```
  0: 0x0082 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=838*)
  1: 0x0086 [0x95] SETUP_EVENT_NPC: Prepare NPC for event (Render.Flags3 = 2*)
  2: 0x0089 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x008A  |
| Data Size    | 6 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                B6 00 13 80 96 00            ......
```

#### Opcodes

```
  0: 0x008A [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2279*)
  1: 0x008E [0x96] UNSET_EVENT_NPC: Restore NPC after event (removes event NPC status)
  2: 0x008F [0x00] END_REQSTACK()
```
