# 17752322 - Dabido-Sorobido

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 204 bytes                 |
| Total Events     | 2                         |
| References Count | 17                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [904](#event-904)     | 0x0001       |    108 |             37 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x29CC      |       10700 |
|       2 | 0x29CD      |       10701 |
|       3 | 0x0002      |           2 |
|       4 | 0x29CE      |       10702 |
|       5 | 0x40000000  |  1073741824 |
|       6 | 0x0008      |           8 |
|       7 | 0x000F      |          15 |
|       8 | 0x29D5      |       10709 |
|       9 | 0x29D6      |       10710 |
|      10 | 0x29D7      |       10711 |
|      11 | 0x29D2      |       10706 |
|      12 | 0x29D3      |       10707 |
|      13 | 0x29D4      |       10708 |
|      14 | 0x29CF      |       10703 |
|      15 | 0x29D0      |       10704 |
|      16 | 0x29D1      |       10705 |

## String References

- **10700**: I'm a chef-in-training, don'taru you know? One day I'll be as famous-wamous as that Rycharde character in Mhaura.
- **10701**: I'm racking my noggin to inventaru a dish that tastes better when eaten with friends. Nothing comes to mind at the momentaru...
- **10702**: You know, I heard there was a new fortune teller in Mhaura. Those guys kind of give me the chilly-willies.
- **10703**: Eureka!
- **10704**: Seeing you and %0 together has spark-warked an idea for a new cooking craze!
- **10705**: Inspiration can strike at the strangest times. Here, try this!
- **10706**: Wait! Could it be!?
- **10707**: Yes! Another marv-warvellous idea for a feeding frenzy! I'll call it "Friendship Pie with Trust Crust"! Doesn't that sound yummy-scrummy?
- **10708**: Since you and %0 were here to witness this culinary triumph, why don'taru you share this in celebration?
- **10709**: Hmmm. Hmmm. Nope, my brill-williance has run dry. There is only so much one Tarutaru can dream up alone.
- **10710**: I'll have to find myself a chum-wummy partner like you have in %0.
- **10711**: In factaru, you two can share this between you. I've lost my appetitaru.

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

### Event 904

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 108 bytes |
| Instructions | 21        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    02 03 10 00 80 00 31  00 1D 01 80 23 02 08 10   ......1....#...
0010: 00 80 00 1C 00 1D 02 80  23 01 28 00 02 08 10 03  ........#.(.....
0020: 80 00 28 00 1D 04 80 23  03 01 10 05 80 21 01 6C  ..(....#.....!.l
0030: 00 02 07 10 06 80 04 5F  00 02 07 10 07 80 04 50  ......._.......P
0040: 00 1D 08 80 23 1D 09 80  23 1D 0A 80 23 01 5C 00  ....#...#...#.\.
0050: 1D 0B 80 23 1D 0C 80 23  1D 0D 80 23 01 6B 00 1D  ...#...#...#.k..
0060: 0E 80 23 1D 0F 80 23 1D  10 80 23 21 00           ..#...#...#!.   
```

#### Opcodes

```
  0: 0x0001 [0x02] IF !(Work_Zone[3] == 1*) GOTO 0x0031
  1: 0x0009 [0x1D] PRINT_EVENT_MESSAGE(message_id=10700*)
    → "I'm a chef-in-training, don'taru you know? One day I'll be as famous-wamous as that Rycharde character in Mhaura."
  2: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000D [0x02] IF !(Work_Zone[8] == 1*) GOTO 0x001C
  4: 0x0015 [0x1D] PRINT_EVENT_MESSAGE(message_id=10701*)
    → "I'm racking my noggin to inventaru a dish that tastes better when eaten with friends. Nothing comes to mind at the momentaru..."
  5: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0019 [0x01] GOTO 0x0028
  7: 0x001C [0x02] IF !(Work_Zone[8] == 2*) GOTO 0x0028
  8: 0x0024 [0x1D] PRINT_EVENT_MESSAGE(message_id=10702*)
    → "You know, I heard there was a new fortune teller in Mhaura. Those guys kind of give me the chilly-willies."
  9: 0x0027 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0028:
 10: 0x0028 [0x03] Work_Zone[1] = 1073741824*
 11: 0x002D [0x21] END_EVENT

SUBROUTINE_005C:
 12: 0x005C [0x01] GOTO 0x006B
 13: 0x005F [0x1D] PRINT_EVENT_MESSAGE(message_id=10703*)
    → "Eureka!"
 14: 0x0062 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0063 [0x1D] PRINT_EVENT_MESSAGE(message_id=10704*)
    → "Seeing you and %0 together has spark-warked an idea for a new cooking craze!"
 16: 0x0066 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x0067 [0x1D] PRINT_EVENT_MESSAGE(message_id=10705*)
    → "Inspiration can strike at the strangest times. Here, try this!"
 18: 0x006A [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_006B:
 19: 0x006B [0x21] END_EVENT

SUBROUTINE_006C:
 20: 0x006C [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x002E [0x01] GOTO 0x006C
```
