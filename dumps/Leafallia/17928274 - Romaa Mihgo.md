# 17928274 - Romaa Mihgo

## Common Data

| Field            | Value               |
|------------------|---------------------|
| Zone             | Leafallia (ID: 281) |
| Block Size       | 104 bytes           |
| Total Events     | 5                   |
| References Count | 6                   |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [78](#event-78)          | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |     20 |              6 |
| [65535.2](#event-655352) | 0x001C       |      7 |              3 |
| [65535.3](#event-655353) | 0x0023       |      7 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0xFFF8E448  |  4294501448 |
|       2 | 0xFFFC4392  |  4294722450 |
|       3 | 0xFFFD72E0  |  4294800096 |
|       4 | 0x0001      |           1 |
|       5 | 0x0000      |           0 |

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

### Event 78

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
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          32 00 80 1F 00 01 80 02          2.......
0010: 80 03 80 1F 01 6F 1E 53  90 11 01 00              .....o.S....    
```

#### Opcodes

```
  0: 0x0008 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x000B [0x1F] MOVE_ENTITY: EventEntity moves to X=-465.848*, Z=-244.846*, Y=-167.200*
  2: 0x0013 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0015 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0016 [0x1E] EventEntity looks at Shadow Lord (ID: 17928275/0x01119053) and starts talking
  5: 0x001B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001C  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                      AB 03 AC 01              ....
0020: 04 80 00                                          ...             
```

#### Opcodes

```
  0: 0x001C [0xAB] EventEntity->Render.Flags0 ^= 0x20000 // Toggle bit 17
  1: 0x001E [0xAC] EventEntity->StatusEvent = 1*
  2: 0x0022 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0023  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          AC 01 05 80 AB  04 00                       .......      
```

#### Opcodes

```
  0: 0x0023 [0xAC] EventEntity->StatusEvent = 0*
  1: 0x0027 [0xAB] EventEntity->Render.Flags0 |= 0x40000 // Set bit 18
  2: 0x0029 [0x00] END_REQSTACK()
```
