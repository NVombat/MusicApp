import { TeamData } from '../../data/Team';
import Card from './Card';
const Team = () => {
  return (
    <div>
      <div className="flex justify-center items-center py-10 text-3xl font-bold">
        Meet Our Team
      </div>
      <div className="flex justify-evenly items-center">
        {TeamData.map((item) => (
          <Card
            key={item.src}
            src={item.src}
            name={item.name}
            desgination={item.designation}
          />
        ))}
      </div>
    </div>
  );
};

export default Team;
