# 17363357 - Refiner Lid

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Palborough Mines (ID: 143) |
| Block Size       | 140 bytes                  |
| Total Events     | 5                          |
| References Count | 6                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [18](#event-18)       | 0x0001       |     28 |             10 |
| [19](#event-19)       | 0x001D       |     18 |              8 |
| [20](#event-20)       | 0x002F       |     18 |              8 |
| [21](#event-21)       | 0x0041       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x003C      |          60 |
|       1 | 0x0255      |         597 |
|       2 | 0x1CD1      |        7377 |
|       3 | 0x1CD2      |        7378 |
|       4 | 0x1CD4      |        7380 |
|       5 | 0x1CD3      |        7379 |

## String References

- **7377**: You see flecks of a shiny material. It looks like they were once $0.
- **7378**: You put in $1 $0 .
- **7379**: No, that doesn't seem right. There must be something else you can put in.
- **7380**: It's full.

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

### Event 18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 28 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4A F0 FF FF 7F 9D F1  08 01 4C 1C 00 80 03 02   J........L.....
0010: 10 01 80 48 02 80 23 4D  1C 00 80 21 00           ...H..#M...!.   
```

#### Opcodes

```
  0: 0x0001 [0x4A] LocalPlayer looks at Refiner Lid (ID: 17363357/0x0108F19D)
  1: 0x000A [0x4C] EventEntity->StatusEvent = 8 // Open door
  2: 0x000B [0x1C] WAIT(60* ticks)
  3: 0x000E [0x03] Work_Zone[2] = 597*
  4: 0x0013 [0x48] [System] [7377*]:
    → "You see flecks of a shiny material. It looks like they were once $0."
  5: 0x0016 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0017 [0x4D] EventEntity->StatusEvent = 9 // Close door
  7: 0x0018 [0x1C] WAIT(60* ticks)
  8: 0x001B [0x21] END_EVENT
  9: 0x001C [0x00] END_REQSTACK()
```

### Event 19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001D   |
| Data Size    | 18 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         42 4A F0               BJ.
0020: FF FF 7F 9D F1 08 01 4C  48 03 80 23 4D 21 00     .......LH..#M!. 
```

#### Opcodes

```
  0: 0x001D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x001E [0x4A] LocalPlayer looks at Refiner Lid (ID: 17363357/0x0108F19D)
  2: 0x0027 [0x4C] EventEntity->StatusEvent = 8 // Open door
  3: 0x0028 [0x48] [System] [7378*]:
    → "You put in $1 $0 ."
  4: 0x002B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x002C [0x4D] EventEntity->StatusEvent = 9 // Close door
  6: 0x002D [0x21] END_EVENT
  7: 0x002E [0x00] END_REQSTACK()
```

### Event 20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 18 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               42                 B
0030: 4A F0 FF FF 7F 9D F1 08  01 4C 48 04 80 23 4D 21  J........LH..#M!
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x002F [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0030 [0x4A] LocalPlayer looks at Refiner Lid (ID: 17363357/0x0108F19D)
  2: 0x0039 [0x4C] EventEntity->StatusEvent = 8 // Open door
  3: 0x003A [0x48] [System] [7380*]:
    → "It's full."
  4: 0x003D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x003E [0x4D] EventEntity->StatusEvent = 9 // Close door
  6: 0x003F [0x21] END_EVENT
  7: 0x0040 [0x00] END_REQSTACK()
```

### Event 21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0041   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:    4A F0 FF FF 7F 9D F1  08 01 48 05 80 23 21 00   J........H..#!.
```

#### Opcodes

```
  0: 0x0041 [0x4A] LocalPlayer looks at Refiner Lid (ID: 17363357/0x0108F19D)
  1: 0x004A [0x48] [System] [7379*]:
    → "No, that doesn't seem right. There must be something else you can put in."
  2: 0x004D [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x004E [0x21] END_EVENT
  4: 0x004F [0x00] END_REQSTACK()
```
