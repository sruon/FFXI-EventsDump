# 16999091 - Merrow Kabukidancer

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Arrapago Reef (ID: 54) |
| Block Size       | 132 bytes              |
| Total Events     | 6                      |
| References Count | 9                      |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [243](#event-243)        | 0x0001       |      7 |              2 |
| [244](#event-244)        | 0x0008       |      7 |              2 |
| [65535.1](#event-655351) | 0x000F       |      7 |              3 |
| [65535.2](#event-655352) | 0x0016       |      7 |              3 |
| [65535.3](#event-655353) | 0x001D       |     25 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0000      |           0 |
|       2 | 0x0028      |          40 |
|       3 | 0xFFF6F825  |  4294375461 |
|       4 | 0x47384     |      291716 |
|       5 | 0xFFFFEFCA  |  4294963146 |
|       6 | 0xFFF73742  |  4294391618 |
|       7 | 0x47580     |      292224 |
|       8 | 0xFFFFF03B  |  4294963259 |

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

### Event 243

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

### Event 244

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          92 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x0008 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000F  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               AB                 .
0010: 03 AC 01 00 80 00                                 ......          
```

#### Opcodes

```
  0: 0x000F [0xAB] EventEntity->Render.Flags0 ^= 0x20000 // Toggle bit 17
  1: 0x0011 [0xAC] EventEntity->StatusEvent = 1*
  2: 0x0015 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0016  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   AC 01  01 80 AB 04 00                 .......   
```

#### Opcodes

```
  0: 0x0016 [0xAC] EventEntity->StatusEvent = 0*
  1: 0x001A [0xAB] EventEntity->Render.Flags0 |= 0x40000 // Set bit 18
  2: 0x001C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001D   |
| Data Size    | 25 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         32 02 80               2..
0020: 1F 00 03 80 04 80 05 80  1F 01 1F 00 06 80 07 80  ................
0030: 08 80 1F 01 6F 00                                 ....o.          
```

#### Opcodes

```
  0: 0x001D [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0020 [0x1F] MOVE_ENTITY: EventEntity moves to X=-591.835*, Z=291.716*, Y=-4.150*
  2: 0x0028 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002A [0x1F] MOVE_ENTITY: EventEntity moves to X=-575.678*, Z=292.224*, Y=-4.037*
  4: 0x0032 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0034 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0035 [0x00] END_REQSTACK()
```
