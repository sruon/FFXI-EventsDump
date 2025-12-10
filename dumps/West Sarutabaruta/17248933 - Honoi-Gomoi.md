# 17248933 - Honoi-Gomoi

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | West Sarutabaruta (ID: 115) |
| Block Size       | 144 bytes                   |
| Total Events     | 6                           |
| References Count | 11                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [919](#event-919)        | 0x0001       |      7 |              2 |
| [920](#event-920)        | 0x0008       |      7 |              2 |
| [65535.1](#event-655351) | 0x000F       |     14 |              4 |
| [65535.2](#event-655352) | 0x001D       |     14 |              4 |
| [65535.3](#event-655353) | 0x002B       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x3B191     |      242065 |
|       2 | 0x4611      |       17937 |
|       3 | 0xFFFFEC7B  |  4294962299 |
|       4 | 0x3B161     |      242017 |
|       5 | 0x38E8      |       14568 |
|       6 | 0xFFFFED78  |  4294962552 |
|       7 | 0x0028      |          40 |
|       8 | 0x3BB71     |      244593 |
|       9 | 0x40E6      |       16614 |
|      10 | 0xFFFFECAA  |  4294962346 |

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

### Event 919

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

### Event 920

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000F   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               32                 2
0010: 00 80 1F 00 01 80 02 80  03 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x000F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0012 [0x1F] MOVE_ENTITY: EventEntity moves to X=242.065*, Z=17.937*, Y=-4.997*
  2: 0x001A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001C [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001D   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         32 00 80               2..
0020: 1F 00 04 80 05 80 06 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x001D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0020 [0x1F] MOVE_ENTITY: EventEntity moves to X=242.017*, Z=14.568*, Y=-4.744*
  2: 0x0028 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002B   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   32 07 80 1F 00             2....
0030: 08 80 09 80 0A 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x002B [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x002E [0x1F] MOVE_ENTITY: EventEntity moves to X=244.593*, Z=16.614*, Y=-4.950*
  2: 0x0036 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0038 [0x00] END_REQSTACK()
```
