# 17257054 - Stone Monument

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Tahrongi Canyon (ID: 117) |
| Block Size       | 76 bytes                  |
| Total Events     | 2                         |
| References Count | 6                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [900](#event-900)     | 0x0001       |     26 |             14 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D15      |        7445 |
|       1 | 0x1D16      |        7446 |
|       2 | 0x1D17      |        7447 |
|       3 | 0x1D18      |        7448 |
|       4 | 0x1D19      |        7449 |
|       5 | 0x1D1A      |        7450 |

## String References

- **7445**: You see a message engraved on the stone:
- **7446**: My survey has run into difficulty here in Tahrongi Canyon. I have had to deal with irregular land, a harsh clime, monsters, and, worst of all, fever.
- **7447**: I thought myself prepared before I ventured into Mindartia, but that did not spare me the fever. Even white magic did nothing.
- **7448**: With faltering steps, I sought shelter from the sun, but there was little shade in sight. Then, it appeared before me: the sun-bleached skeleton of an ancient wyrm.
- **7449**: I approached, and found this cave. I soon discovered that the water from a nearby cactus helped reduce my fever. As I recovered, I decided to name my saviors.
- **7450**: In memory of my old friends, Gilbo, Madge, and Navil: victims of a heat wave that struck in the midst of a brotherly quarrel. --Enid Ironheart, 774 Crystal Era.

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

### Event 900

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 26 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    48 00 80 23 48 01 80  23 48 02 80 23 48 03 80   H..#H..#H..#H..
0010: 23 48 04 80 23 48 05 80  23 21 00                 #H..#H..#!.     
```

#### Opcodes

```
  0: 0x0001 [0x48] [System] [7445*]:
    → "You see a message engraved on the stone:"
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x48] [System] [7446*]:
    → "My survey has run into difficulty here in Tahrongi Canyon. I have had to deal with irregular land, a harsh clime, monsters, and, worst of all, fever."
  3: 0x0008 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0009 [0x48] [System] [7447*]:
    → "I thought myself prepared before I ventured into Mindartia, but that did not spare me the fever. Even white magic did nothing."
  5: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x000D [0x48] [System] [7448*]:
    → "With faltering steps, I sought shelter from the sun, but there was little shade in sight. Then, it appeared before me: the sun-bleached skeleton of an ancient wyrm."
  7: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0011 [0x48] [System] [7449*]:
    → "I approached, and found this cave. I soon discovered that the water from a nearby cactus helped reduce my fever. As I recovered, I decided to name my saviors."
  9: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0015 [0x48] [System] [7450*]:
    → "In memory of my old friends, Gilbo, Madge, and Navil: victims of a heat wave that struck in the midst of a brotherly quarrel. --Enid Ironheart, 774 Crystal Era."
 11: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0019 [0x21] END_EVENT
 13: 0x001A [0x00] END_REQSTACK()
```
