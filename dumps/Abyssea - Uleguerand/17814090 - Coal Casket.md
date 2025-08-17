# 17814090 - Coal Casket

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Abyssea - Uleguerand (ID: 253) |
| Block Size       | 80 bytes                       |
| Total Events     | 4                              |
| References Count | 4                              |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [252](#event-252)     | 0x0001       |      1 |              1 |
| [255](#event-255)     | 0x0002       |     12 |              6 |
| [256](#event-256)     | 0x000E       |     15 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x06B4      |        1716 |
|       1 | 0x1EC2      |        7874 |
|       2 | 0x1EC3      |        7875 |
|       3 | 0x1EC5      |        7877 |

## String References

- **7874**: You open the casket and deposit a pack of $3 within.
- **7875**: The casket contains an ample supply of $3.
- **7877**: There seems to be no need for replenishment at this time.

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

### Event 255

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 12 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       03 02 10 00 80 42  48 01 80 23 21 00          .....BH..#!.  
```

#### Opcodes

```
  0: 0x0002 [0x03] Work_Zone[2] = 1716*
  1: 0x0007 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0008 [0x48] [System] [7874*]:
    → "You open the casket and deposit a pack of $3 within."
  3: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000C [0x21] END_EVENT
  5: 0x000D [0x00] END_REQSTACK()
```

### Event 256

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000E   |
| Data Size    | 15 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            03 02                ..
0010: 10 00 80 48 02 80 23 48  03 80 23 21 00           ...H..#H..#!.   
```

#### Opcodes

```
  0: 0x000E [0x03] Work_Zone[2] = 1716*
  1: 0x0013 [0x48] [System] [7875*]:
    → "The casket contains an ample supply of $3."
  2: 0x0016 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0017 [0x48] [System] [7877*]:
    → "There seems to be no need for replenishment at this time."
  4: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x001B [0x21] END_EVENT
  6: 0x001C [0x00] END_REQSTACK()
```
