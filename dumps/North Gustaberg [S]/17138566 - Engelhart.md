# 17138566 - Engelhart

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | North Gustaberg [S] (ID: 88) |
| Block Size       | 60 bytes                     |
| Total Events     | 4                            |
| References Count | 2                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [13](#event-13)          | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |      6 |              4 |
| [65535.2](#event-655352) | 0x000E       |      6 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1FA6      |        8102 |
|       1 | 0x1FA7      |        8103 |

## String References

- **8102**: With you at our side, and bonds of friendship stronger than mythril as our strength, there is no storm our Republic cannot weather.
- **8103**: Together, let us forge our future. A future as bright as the brightest dawn...

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

### Event 13

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 6 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          48 00 80 23 23 00                H..##.  
```

#### Opcodes

```
  0: 0x0008 [0x48] [System] [8102*]:
    → "With you at our side, and bonds of friendship stronger than mythril as our strength, there is no storm our Republic cannot weather."
  1: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000E  |
| Data Size    | 6 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            48 01                H.
0010: 80 23 23 00                                       .##.            
```

#### Opcodes

```
  0: 0x000E [0x48] [System] [8103*]:
    → "Together, let us forge our future. A future as bright as the brightest dawn..."
  1: 0x0011 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0012 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0013 [0x00] END_REQSTACK()
```
