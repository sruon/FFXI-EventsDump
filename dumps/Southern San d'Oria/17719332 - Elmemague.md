# 17719332 - Elmemague

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Southern San d'Oria (ID: 230) |
| Block Size       | 140 bytes                     |
| Total Events     | 6                             |
| References Count | 10                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [33](#event-33)          | 0x0001       |     16 |              3 |
| [65535.1](#event-655351) | 0x0011       |     14 |              4 |
| [65535.2](#event-655352) | 0x001F       |      6 |              2 |
| [65535.3](#event-655353) | 0x0025       |      6 |              2 |
| [65535.4](#event-655354) | 0x002B       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFE41BE  |  4294853054 |
|       1 | 0x6927      |       26919 |
|       2 | 0xFFFFF830  |  4294965296 |
|       3 | 0x0F22      |        3874 |
|       4 | 0x0028      |          40 |
|       5 | 0xFFFE77E4  |  4294866916 |
|       6 | 0x7C3E      |       31806 |
|       7 | 0xFFFE72C6  |  4294865606 |
|       8 | 0x4803      |       18435 |
|       9 | 0xFFFFF831  |  4294965297 |

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

### Event 33

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    94 01 F8 FF FF 7F 37  00 80 01 80 02 80 03 80   ......7........
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-114.242*, z=26.919*, y=-2.000*, direction=340.5°*
  2: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    32 04 80 1F 00 05 80  06 80 02 80 1F 01 00      2............. 
```

#### Opcodes

```
  0: 0x0011 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=-100.380*, Z=31.806*, Y=-2.000*
  2: 0x001C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001F  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               1E                 .
0020: 22 60 0E 01 00                                    "`...           
```

#### Opcodes

```
  0: 0x001F [0x1E] EventEntity looks at Deraquien (ID: 17719330/0x010E6022) and starts talking
  1: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0025  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                1E F0 FF  FF 7F 00                      ......     
```

#### Opcodes

```
  0: 0x0025 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x002A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002B   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   32 04 80 1F 00             2....
0030: 07 80 08 80 09 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x002B [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x002E [0x1F] MOVE_ENTITY: EventEntity moves to X=-101.690*, Z=18.435*, Y=-1.999*
  2: 0x0036 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0038 [0x00] END_REQSTACK()
```
