# 17236383 - Dynamis Lord

## Common Data

| Field            | Value               |
|------------------|---------------------|
| Zone             | Xarcabard (ID: 112) |
| Block Size       | 112 bytes           |
| Total Events     | 5                   |
| References Count | 7                   |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65](#event-65)          | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |     10 |              2 |
| [65535.2](#event-655352) | 0x0012       |     13 |              3 |
| [65535.3](#event-655353) | 0x001F       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0064      |         100 |
|       2 | 0x005A      |          90 |
|       3 | 0x000D      |          13 |
|       4 | 0xFFF9A884  |  4294551684 |
|       5 | 0x505F      |       20575 |
|       6 | 0xFFFF5421  |  4294923297 |

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

### Event 65

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0008   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          6C 9F 01 07 01 00 80 01          l.......
0010: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0008 [0x6C] FADE_ENTITY_COLOR(entity_id=Dynamis Lord (ID: 17236383/0x0107019F), end_alpha=0*, fade_time=100*)
  1: 0x0011 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0012   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       1C 02 80 6C 9F 01  07 01 01 80 01 80 00       ...l......... 
```

#### Opcodes

```
  0: 0x0012 [0x1C] WAIT(90* ticks)
  1: 0x0015 [0x6C] FADE_ENTITY_COLOR(entity_id=Dynamis Lord (ID: 17236383/0x0107019F), end_alpha=100*, fade_time=100*)
  2: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               32                 2
0020: 03 80 1F 00 04 80 05 80  06 80 1F 01 6F 00        ............o.  
```

#### Opcodes

```
  0: 0x001F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0022 [0x1F] MOVE_ENTITY: EventEntity moves to X=-415.612*, Z=20.575*, Y=-43.999*
  2: 0x002A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x002D [0x00] END_REQSTACK()
```
