# 17814089 - Coal Casket

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Abyssea - Uleguerand (ID: 253) |
| Block Size       | 84 bytes                       |
| Total Events     | 4                              |
| References Count | 3                              |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [252](#event-252)     | 0x0001       |     11 |              5 |
| [253](#event-253)     | 0x000C       |     12 |              6 |
| [254](#event-254)     | 0x0018       |     15 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x06B4      |        1716 |
|       1 | 0x1EC3      |        7875 |
|       2 | 0x1EC4      |        7876 |

## String References

- **7875**: The casket contains an ample supply of $3.
- **7876**: You cannot carry any more $3.

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

### Event 252

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 02 10 00 80 48 01  80 23 21 00               .....H..#!.    
```

#### Opcodes

```
  0: 0x0001 [0x03] Work_Zone[2] = 1716*
  1: 0x0006 [0x48] [System] [7875*]:
    → "The casket contains an ample supply of $3."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x21] END_EVENT
  4: 0x000B [0x00] END_REQSTACK()
```

### Event 253

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 12 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      03 02 10 00              ....
0010: 80 42 48 01 80 23 21 00                           .BH..#!.        
```

#### Opcodes

```
  0: 0x000C [0x03] Work_Zone[2] = 1716*
  1: 0x0011 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0012 [0x48] [System] [7875*]:
    → "The casket contains an ample supply of $3."
  3: 0x0015 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0016 [0x21] END_EVENT
  5: 0x0017 [0x00] END_REQSTACK()
```

### Event 254

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0018   |
| Data Size    | 15 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          03 02 10 00 80 48 01 80          .....H..
0020: 23 48 02 80 23 21 00                              #H..#!.         
```

#### Opcodes

```
  0: 0x0018 [0x03] Work_Zone[2] = 1716*
  1: 0x001D [0x48] [System] [7875*]:
    → "The casket contains an ample supply of $3."
  2: 0x0020 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0021 [0x48] [System] [7876*]:
    → "You cannot carry any more $3."
  4: 0x0024 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0025 [0x21] END_EVENT
  6: 0x0026 [0x00] END_REQSTACK()
```
